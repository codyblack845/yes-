# Verification report

Checked against the live public Stonewall Fellowship website on October 12, 2026.

## Content retained

The comparison covered every page reachable through the original website’s internal links: the homepage, article archive, and all seven complete essays (nine pages total). No original visible page text was deleted or replaced. All original link targets, section IDs, contact details, social links, newsletter fields, and form settings are retained. The homepage adds a skip link and a Weekly Letter shortcut.

All 18 unique image files referenced by the original pages are present and byte-for-byte identical to the originals. The visible shield and favicon were intentionally replaced with the previously discussed preview cutout; the old emblem files remain in the repository. Colors, typography, decorative framing, and layout are the requested design changes.

The original site’s robots.txt and sitemap.xml both returned 404; they revealed no additional pages. This audit covers the publicly linked website, not private or unlinked pages that cannot be discovered from it.

## Functional verification

| Check | Result |
| --- | --- |
| Nine pages at desktop, tablet, mobile, and small mobile widths (1440, 768, 390, and 320 pixels) | 36 page checks passed |
| Internal links and section anchors | 115 checks passed |
| Page and asset loading | No missing local resources |
| Images and loaded fonts | Passed |
| Horizontal overflow and duplicate element IDs | None found |
| Mobile menu opening, closing, and article navigation | Passed |
| Homepage → archive → complete essay → archive | Passed |
| Newsletter required names and email | Passed |
| Newsletter email format and consent validation | Passed |
| Newsletter POST destination and submitted fields | Passed with the outgoing request intercepted |
| Browser JavaScript errors | None found |

The newsletter test used a reserved .invalid email address and intercepted the outgoing request before it reached the provider. It verified the browser’s request destination, method, first and last names, email, consent, subject, and honeypot fields. The test response was simulated; no real signup or email was sent.

## Not confirmed

Actual delivery of the signup notification to stonewallfellowship1@outlook.com, provider account activation, and availability of the external social profiles were not verified. The existing FormSubmit endpoint is preserved, but this cloud environment’s network policy rejected a read-only request to formsubmit.co. An authorized test submission and confirmation from the site owner’s Outlook inbox are needed to verify actual delivery. The existing form emails a subscription request to the site owner; automated distribution of future weekly letters is outside this static website’s form, as on the original site.

The redesign has not been deployed to the live Netlify site. Production deployment and a post-deployment smoke check remain separate steps. The original master logo is still needed for exact production artwork fidelity, as documented in the preview.

## Recorded evidence

- [Page-by-page content comparison](preview/content-audit.json)
- [Browser check results](preview/browser-audit.json)
- [Actual browser screenshots](README.md)
