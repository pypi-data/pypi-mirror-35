import six

CRLF = '\r\n'
NL = CRLF

if six.PY2:
    class BatchPolicy(object):
        pass

    from email.header import Header as OldHeader
    from email.header import _max_append
    from email.generator import Generator as OldGen
    from email.generator import _make_boundary, fcre, _is8bitstring

    from StringIO import StringIO

    class Header(OldHeader):

        def _encode_chunks(self, newchunks, maxlinelen):
            # MIME-encode a header with many different charsets and/or encodings.
            #
            # Given a list of pairs (string, charset), return a MIME-encoded
            # string suitable for use in a header field.  Each pair may have
            # different charsets and/or encodings, and the resulting header will
            # accurately reflect each setting.
            #
            # Each encoding can be email.utils.QP (quoted-printable, for
            # ASCII-like character sets like iso-8859-1), email.utils.BASE64
            # (Base64, for non-ASCII like character sets like KOI8-R and
            # iso-2022-jp), or None (no encoding).
            #
            # Each pair will be represented on a separate line; the resulting
            # string will be in the format:
            #
            # =?charset1?q?Mar=EDa_Gonz=E1lez_Alonso?=\n
            #  =?charset2?b?SvxyZ2VuIEL2aW5n?="
            chunks = []
            for header, charset in newchunks:
                if not header:
                    continue
                if charset is None or charset.header_encoding is None:
                    s = header
                else:
                    s = charset.header_encode(header)
                # Don't add more folding whitespace than necessary
                if chunks and chunks[-1].endswith(' '):
                    extra = ''
                else:
                    extra = ' '
                _max_append(chunks, s, maxlinelen, extra)
            joiner = NL + self._continuation_ws
            return joiner.join(chunks)
    
    class Generator(OldGen):

        def __init__(self, *args, **kwargs):
            OldGen.__init__(self, *args, **kwargs)

        def _write_headers(self, msg):
            for h, v in msg.items():
                print >> self._fp, '%s:' % h,
                if self._maxheaderlen == 0:
                    # Explicit no-wrapping
                    print >> self._fp, v
                elif isinstance(v, Header):
                    # Header instances know what to do
                    print >> self._fp, v.encode()
                elif _is8bitstring(v):
                    # If we have raw 8bit data in a byte string, we have no idea
                    # what the encoding is.  There is no safe way to split this
                    # string.  If it's ascii-subset, then we could do a normal
                    # ascii split, but if it's multibyte then we could break the
                    # string.  There's no way to know so the least harm seems to
                    # be to not split the string and risk it being too long.
                    print >> self._fp, v
                else:
                    # Header's got lots of smarts, so use it.  Note that this is
                    # fundamentally broken though because we lose idempotency when
                    # the header string is continued with tabs.  It will now be
                    # continued with spaces.  This was reversedly broken before we
                    # fixed bug 1974.  Either way, we lose.
                    print >> self._fp, Header(
                        v, maxlinelen=self._maxheaderlen, header_name=h).encode()
            # A blank line always separates headers from body
            print >> self._fp

        def _handle_multipart(self, msg):
            # The trick here is to write out each part separately, merge them all
            # together, and then make sure that the boundary we've chosen isn't
            # present in the payload.
            msgtexts = []
            subparts = msg.get_payload()
            if subparts is None:
                subparts = []
            elif isinstance(subparts, basestring):
                # e.g. a non-strict parse of a message with no starting boundary.
                self._fp.write(subparts)
                return
            elif not isinstance(subparts, list):
                # Scalar payload
                subparts = [subparts]
            for part in subparts:
                s = StringIO()
                g = self.clone(s)
                g.flatten(part, unixfrom=False)
                msgtexts.append(s.getvalue())
            # BAW: What about boundaries that are wrapped in double-quotes?
            boundary = msg.get_boundary()
            if not boundary:
                # Create a boundary that doesn't appear in any of the
                # message texts.
                alltext = NL.join(msgtexts)
                boundary = _make_boundary(alltext)
                msg.set_boundary(boundary)
            # If there's a preamble, write it out, with a trailing CRLF
            if msg.preamble is not None:
                if self._mangle_from_:
                    preamble = fcre.sub('>From ', msg.preamble)
                else:
                    preamble = msg.preamble
                print >> self._fp, preamble
            # dash-boundary transport-padding CRLF
            print >> self._fp, '--' + boundary
            # body-part
            if msgtexts:
                self._fp.write(msgtexts.pop(0))
            # *encapsulation
            # --> delimiter transport-padding
            # --> CRLF body-part
            for body_part in msgtexts:
                # delimiter transport-padding CRLF
                print >> self._fp, NL + '--' + boundary
                # body-part
                self._fp.write(body_part)
            # close-delimiter transport-padding
            self._fp.write(NL + '--' + boundary + '--' + NL)
            if msg.epilogue is not None:
                if self._mangle_from_:
                    epilogue = fcre.sub('>From ', msg.epilogue)
                else:
                    epilogue = msg.epilogue
                self._fp.write(epilogue)

        def _handle_message_delivery_status(self, msg):
            # We can't just write the headers directly to self's file object
            # because this will leave an extra newline between the last header
            # block and the boundary.  Sigh.
            blocks = []
            for part in msg.get_payload():
                s = StringIO()
                g = self.clone(s)
                g.flatten(part, unixfrom=False)
                text = s.getvalue()
                lines = text.split('\n')
                # Strip off the unnecessary trailing empty line
                if lines and lines[-1] == '':
                    blocks.append(NL.join(lines[:-1]))
                else:
                    blocks.append(text)
            # Now join all the blocks with an empty line.  This has the lovely
            # effect of separating each block with an empty line, but not adding
            # an extra one after the last one.
            self._fp.write(NL.join(blocks))


elif six.PY3:
    from email.generator import Generator
    from email._policybase import Compat32

    class BatchPolicy(Compat32):
        linesep = CRLF



