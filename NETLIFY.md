# Upload to Netlify

This package includes the updated mobile layout and the requested removal of the Home, Church, and Community decorative section.

This is a static website. No dependency installation, build command, database, or server configuration is required for a manual upload.

1. Download **netlify-upload.zip** from this repository.
2. Extract it. The extracted folder must contain `index.html` directly, alongside `styles.css`, `articles.css`, `refined.css`, `script.js`, `articles/`, and `assets/`.
3. When ready to publish, open your existing Netlify project, go to **Deploys**, and drag that extracted folder into the manual upload area. Use the existing project to retain your domain configuration.

The ZIP includes the homepage, article archive, all seven complete essays, all website images, and self-hosted fonts. It excludes Git metadata, screenshots, validation reports, setup tools, and test-submission files. Do not upload GitHub's entire repository archive; use this prepared ZIP.

## Package verification

The extracted ZIP passed integrity and source-byte checks for all 38 packaged files. All nine pages returned HTTP 200, and browser checks passed for image/font loading, mobile navigation, the article archive, a complete essay, and the unchanged newsletter form settings. [Recorded package checks](preview/netlify-package-audit.json).

## Check after uploading

Visit the homepage, open the article archive and a complete essay, use the mobile menu, and check the newsletter/contact area. Existing article addresses and the original email and social links are retained.

The newsletter continues to send subscription requests through the existing FormSubmit endpoint. Signup validation and the browser's submission data have passed testing, but real delivery to the Outlook inbox remains unverified. The authorized test notification has not been sent because the cloud environment still blocks the provider.

The package uses the artwork and typography shown in the accepted preview. The shield is the previously documented derived cutout; replace it with original master artwork if exact logo fidelity is required before publication.

## Refresh the upload ZIP

From the repository root, run:

```sh
python3 tools/build_netlify_package.py
```

This recreates `netlify-upload.zip` from the current site files. Website changes require regenerating the ZIP before the next upload.
