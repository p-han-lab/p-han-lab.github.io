# HAN Lab — Health, Adaptation & Nitrogen

This is a ready-to-publish static website for the GitHub repository **CityUHK-han-lab**. The homepage, `index.html`, is directly at the repository root. There is no Python build, npm installation, or custom workflow to configure.

## Publish the website

1. Create a **public** GitHub repository named **CityUHK-han-lab**, using the **main** branch. A public repository supports Pages on GitHub Free.
2. Extract **CityUHK-han-lab.zip** on your computer. On GitHub choose **Add file → Upload files** and upload the **contents** of the extracted folder. Keep the `css`, `js`, and `img` folders intact. Commit the upload to `main`.
3. On the repository's **Code** tab, confirm that you can see `index.html` immediately in the file list. It must not be inside `dist` or another `CityUHK-han-lab` folder. Upload the extracted files, not the ZIP file itself.
4. Open **Settings → Pages**. Under **Build and deployment**, choose:

   | Setting | Value |
   | --- | --- |
   | Source | **Deploy from a branch** |
   | Branch | **main** |
   | Folder | **/(root)** |

   Click **Save**.
5. Wait for GitHub's Pages deployment to finish. Open **Settings → Pages → Visit site** to see your website. GitHub provides the final link there.

The expected address is:

```text
https://YOUR-GITHUB-USERNAME.github.io/CityUHK-han-lab/
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub account name. After this one-time setup, commits to `main` are published automatically.

**Uploading files alone does not enable GitHub Pages. Step 4 is required.** The repository page on `github.com` shows source files; the website is served from `github.io`.

## If you already uploaded the earlier package

- Use the files in this package at the repository root.
- Remove the earlier custom workflow `.github/workflows/pages.yml` from that repository so it does not overwrite this directly published website.
- Change the Pages source from **GitHub Actions** to **Deploy from a branch**, then choose **main** and **/(root)**.
- The old `build.py`, `template`, `data`, and `dist` folders are not used by this package. You can keep a separate backup of that earlier source package for future rebuilding.

## What the repository should contain

```text
CityUHK-han-lab/
├── index.html          Homepage
├── research.html       Four research themes
├── people.html         PI portrait and group members
├── publications.html   Selected papers and Google Scholar link
├── news.html           News and events
├── gallery.html        Group photos (ready to add later)
├── contact.html        Contact information
├── css/
│   └── custom.css
├── js/
│   ├── cityu.config.js
│   └── custom.js
├── img/
│   └── penny-han.jpg
├── .nojekyll
├── README.md
└── ASSET-SOURCES.md
```

The hidden `.nojekyll` file tells GitHub to serve these files directly. On a Mac, **Command + Shift + .** shows hidden files in Finder. You can also create an empty file named `.nojekyll` using GitHub's **Add file → Create new file**.

## Future edits

- Edit the corresponding `.html` file directly; there is no build step.
- To update news on both pages, edit `index.html` and `news.html`.
- Add member photos and email addresses in `people.html`, using the examples below.
- Add group photographs and captions in `gallery.html`.
- Change colors, fonts and layout in `css/custom.css`.
- Keep local links relative (for example `people.html` and `img/penny-han.jpg`), without a leading slash, so they work under `/CityUHK-han-lab/`.
- Commit changes to `main`; GitHub Pages will update the site.

The shared CityUHK template styles, scripts and logos load from the original CityUHK servers. Your PI photo is included in this package. The website needs internet access to load those shared assets.

## Add member photos and email addresses

The PI and visiting scholar retain their visible profile links. For other current members, clicking either the name or portrait reveals the member's email address. The email is hidden on initial page load. The eight supplied member portraits and email addresses are populated. An empty field on any future entry reveals “Email to be added.”

1. Upload a portrait to `img/`, for example `img/linao-zhu.jpg`.
2. Find the member in `people.html`. Inside their `member-photo-button`, replace only the `<span class="photo-placeholder" ...>...</span>` with the image below. Keep the surrounding button, its attributes, and the member's name button intact:

```html
<img class="member-photo" src="img/linao-zhu.jpg"
     alt="Mr. Linao Zhu" width="1279" height="1706" loading="lazy">
```

3. On that member's opening `<article class="member" data-email="">` tag, put the real email address between the empty quotes. For example, replace the illustrative address below with the member's actual address:

```html
<article class="member" data-email="member@example.org">
```

No separate website link is needed for these members. The email link is generated automatically when clicked. The visitor can click the displayed address to compose an email, and click the name or photo again to hide it. The buttons also work with a keyboard.

Member portraits display at 140 × 210 pixels, with the visiting scholar's square portrait at 140 × 140 pixels. The PI portrait stays larger at 150 pixels wide. Dr. Weifu Yan and Dr. Boyu Peng are listed under **Former members**, each labeled **Former postdoc**.

Keep corresponding updates in `template/people.htm` and `dist/people.html` when maintaining those source copies, so rebuilding does not restore older member details.

The visiting scholar’s supplied portrait is included as `img/uli-klumper.png` (under `dist/` in the source package). Replace this image to update his photo.

## Add Gallery photos

1. Create an `img/gallery/` folder and upload your photos there.
2. In `gallery.html`, remove the entire `<div class="gallery-empty">...</div>` block.
3. Inside `<div class="gallery-grid">`, add one figure per photo. A commented example is already included in the file. Copy it outside the comment, then update the image path, description, and caption:

```html
<figure class="gallery-item">
  <a href="img/gallery/group-photo.jpg">
    <img src="img/gallery/group-photo.jpg"
         alt="Describe the people or activity shown" loading="lazy">
  </a>
  <figcaption>Your caption · Month Year</figcaption>
</figure>
```

Clicking a photo opens its full-size image. Uploading an image alone does not add it to the Gallery; its HTML figure must also be added.

## Updating this version on your existing GitHub website

Extract the ZIP and upload its contents to the same repository locations, replacing matching files. This update changes `people.html`, `css/custom.css`, and `js/custom.js`. All seven HTML pages contain refreshed asset references, so upload the complete package while keeping the `css`, `js`, and `img` folders intact. Commit the upload to your configured Pages branch.

## If the website does not appear

- Check that `index.html` is at the repository root and the upload is committed to `main`.
- Confirm **Settings → Pages → Deploy from a branch → main → /(root)** and click **Save**.
- Use the **Visit site** link on the Pages settings screen.
- The **Actions** tab shows GitHub's built-in Pages deployment status, even though this package has no custom workflow file.
- If the deployment fails, open that run to see the reported error.

## Reference

[GitHub: configuring a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
