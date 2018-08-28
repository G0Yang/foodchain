# This Python file uses the following encoding: utf-8

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from Crypto.PublicKey import RSA
# Generate a CSR



keyname = "rootCA"

private_key_file = open(keyname+'_private.pem', 'r')
private_key = RSA.importKey(private_key_file.read(), passphrase='password')
public_key_file = open(keyname+'_public.pem', 'r')
public_key = RSA.importKey(public_key_file.read())


print(private_key)
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who we are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
])).add_extension(
    x509.SubjectAlternativeName([
        # Describe what sites we want this certificate for.
        x509.DNSName(u"mysite.com"),
        x509.DNSName(u"www.mysite.com"),
        x509.DNSName(u"subdomain.mysite.com"),
    ]),
    critical=False,
# Sign the CSR with our private key.
).sign(private_key, hashes.SHA256(), default_backend())
# Write our CSR out to disk.
with open(keyname+"_csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))
