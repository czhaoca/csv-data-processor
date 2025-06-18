# Code Signing Guide

## Windows SmartScreen Warning

The "Windows protected your PC" warning appears because the executable isn't digitally signed. Here's how to resolve it:

## For Users (Immediate Solution)

1. **Bypass the warning**:
   - Click "More info" in the SmartScreen dialog
   - Click "Run anyway"

2. **Unblock the file**:
   - Right-click the downloaded .exe file
   - Select "Properties"
   - Check "Unblock" at the bottom
   - Click "OK"

## For Developers (Permanent Solution)

### 1. Code Signing Certificate

Purchase a code signing certificate from a trusted Certificate Authority:

- **DigiCert**: $474/year (EV), $319/year (OV)
- **Sectigo**: $199/year (OV)
- **GlobalSign**: $249/year (OV)

### 2. GitHub Secrets Setup

Add these secrets to your GitHub repository:

1. `WINDOWS_CERT_BASE64`: Base64 encoded .p12 certificate file
2. `WINDOWS_CERT_PASSWORD`: Certificate password

```bash
# Convert certificate to base64
base64 -i your-cert.p12 -o cert-base64.txt
```

### 3. Automatic Signing

The GitHub Actions workflow is already configured to sign executables when certificates are available.

### 4. Alternative Solutions

#### A. Windows Store Distribution
- Submit to Microsoft Store (requires developer account: $19)
- Automatic signing and trusted distribution

#### B. Reputation Building
- Download and run the unsigned executable repeatedly
- Microsoft SmartScreen learns over time
- Eventually stops showing warnings

#### C. Enterprise Distribution
- Use Group Policy to whitelist the application
- Deploy via enterprise software distribution tools

## Building Reputation

Even with code signing, new certificates may trigger warnings initially. Microsoft SmartScreen considers:

- **Certificate reputation**: How long the certificate has been used
- **Download volume**: How many users have downloaded safely
- **User feedback**: Positive user interactions

## Cost-Effective Options

1. **Open Source Certificate**: Some programs offer free certificates for open source projects
2. **Community builds**: Let users build from source
3. **Package managers**: Distribute via Chocolatey, Scoop, or winget

## Implementation Status

- ✅ GitHub Actions workflow supports code signing
- ⚠️ Requires purchasing a code signing certificate
- ⚠️ Certificate secrets need to be added to repository

## Next Steps

1. Purchase a code signing certificate
2. Add certificate secrets to GitHub repository
3. Test signing process
4. Update documentation for users