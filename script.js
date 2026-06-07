const navToggle = document.querySelector(".nav-toggle");
const primaryNav = document.querySelector(".primary-nav");

if (navToggle && primaryNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = primaryNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  primaryNav.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      primaryNav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    }
  });
}

function displayNameFromFile(filename) {
  return filename
    .replace(/\.[^/.]+$/, "")
    .replace(/[-_]+/g, " ")
    .trim();
}

async function loadCertificates() {
  const container = document.querySelector("#certificate-list");
  if (!container) {
    return;
  }

  try {
    const response = await fetch("assets/certificates-manifest.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Certificate manifest request failed: ${response.status}`);
    }

    const certificates = await response.json();
    if (!Array.isArray(certificates) || certificates.length === 0) {
      container.innerHTML = '<p class="empty-state">No certificates found yet. Add files to the Certificates folder and run the build script.</p>';
      return;
    }

    container.innerHTML = certificates
      .map((certificate) => {
        const name = certificate.displayName || displayNameFromFile(certificate.filename || "Certificate");
        const href = certificate.path;
        return `
          <article class="certificate-card">
            <div>
              <h3>${name}</h3>
              <p>${certificate.type || "Certificate file"}</p>
            </div>
            <div class="certificate-actions">
              <a href="${href}" target="_blank" rel="noopener">View/Open</a>
              <a href="${href}" download>Download</a>
            </div>
          </article>
        `;
      })
      .join("");
  } catch (error) {
    container.innerHTML = '<p class="empty-state">Certificates could not be loaded. Run the build script to generate the manifest.</p>';
    console.error(error);
  }
}

loadCertificates();
