const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      navLinks.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

async function loadJson(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`Unable to load ${path}`);
  }
  return response.json();
}

function renderEvidence(items) {
  const grid = document.querySelector("#evidence-grid");
  if (!grid) {
    return;
  }

  grid.innerHTML = "";
  for (const item of items) {
    const card = document.createElement("article");
    card.className = "evidence-card";
    card.innerHTML = `
      <img src="${item.src}" alt="${item.title}">
      <div>
        <h3>${item.title}</h3>
        <p>${item.caption}</p>
      </div>
    `;
    grid.append(card);
  }
}

function renderCertificates(items) {
  const grid = document.querySelector("#certificate-grid");
  if (!grid) {
    return;
  }

  grid.innerHTML = "";
  if (!items.length) {
    const card = document.createElement("article");
    card.className = "certificate-card";
    card.innerHTML = `
      <h3>No certificates found</h3>
      <p>Add PDF or image files to the Certificates folder and regenerate the static site.</p>
    `;
    grid.append(card);
    return;
  }

  for (const item of items) {
    const card = document.createElement("article");
    card.className = "certificate-card";
    card.innerHTML = `
      <h3>${item.title}</h3>
      <p>${item.type} learning evidence</p>
      <a href="${item.href}" target="_blank" rel="noopener">Open certificate</a>
    `;
    grid.append(card);
  }
}

function renderProfileImages(items) {
  const heroProfile = document.querySelector("#hero-profile");
  const aboutGrid = document.querySelector("#about-profile-images");
  const galleryGrid = document.querySelector("#profile-gallery");
  const gallerySection = document.querySelector("#gallery");

  if (!items.length) {
    if (gallerySection) {
      gallerySection.hidden = true;
    }
    return;
  }

  const createImage = (item, alt) => {
    const image = document.createElement("img");
    image.src = item.src;
    image.alt = alt;
    image.loading = "lazy";
    image.decoding = "async";
    return image;
  };

  if (heroProfile) {
    heroProfile.innerHTML = "";
    const image = createImage(items[0], `${items[0].title} portrait`);
    image.loading = "eager";
    heroProfile.append(image);
  }

  if (aboutGrid) {
    aboutGrid.innerHTML = "";
    for (const item of items.slice(0, 3)) {
      const figure = document.createElement("figure");
      figure.append(createImage(item, item.title));
      aboutGrid.append(figure);
    }
  }

  if (galleryGrid) {
    galleryGrid.innerHTML = "";
    for (const item of items) {
      const card = document.createElement("article");
      card.className = "profile-gallery-card card";

      const figure = document.createElement("figure");
      figure.append(createImage(item, item.title));

      const caption = document.createElement("figcaption");
      const heading = document.createElement("h3");
      heading.textContent = item.title;
      const description = document.createElement("p");
      description.textContent = "Portfolio image.";
      caption.append(heading, description);
      figure.append(caption);
      card.append(figure);
      galleryGrid.append(card);
    }
  }
}

async function renderContributionVideo() {
  const videoCard = document.querySelector("#video");
  const videoSlot = document.querySelector("#contribution-video");
  const source = videoCard?.dataset.videoSrc;

  if (!videoSlot || !source) {
    return;
  }

  try {
    const response = await fetch(source, { method: "HEAD", cache: "no-store" });
    if (!response.ok) {
      throw new Error("Contribution video not found");
    }

    videoSlot.innerHTML = `
      <video controls preload="metadata" aria-label="Individual contribution video">
        <source src="${source}" type="video/mp4">
        <a href="${source}">Open contribution video</a>
      </video>
      <a class="video-link" href="${source}" target="_blank" rel="noopener">Open video in a new tab</a>
    `;
  } catch {
    videoSlot.innerHTML = `
      <p>Contribution video file is not available yet.</p>
      <p>Add <code>assets/videos/contribution-video.mp4</code> and regenerate the static site.</p>
    `;
  }
}

Promise.all([
  loadJson("profile-images.json").then(renderProfileImages),
  loadJson("evidence.json").then(renderEvidence),
  loadJson("certificates.json").then(renderCertificates),
]).catch((error) => {
  console.error(error);
});

renderContributionVideo();
