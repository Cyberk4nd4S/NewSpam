import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))