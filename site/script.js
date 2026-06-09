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

Promise.all([
  loadJson("evidence.json").then(renderEvidence),
  loadJson("certificates.json").then(renderCertificates),
]).catch((error) => {
  console.error(error);
});
