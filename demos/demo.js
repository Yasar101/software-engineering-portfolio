(() => {
  const config = window.DEMO || {};
  if (config.name) {
    const header = document.createElement("header");
    header.className = "demo-header";
    const brand = document.createElement("a");
    brand.className = "brand";
    brand.href = config.home || "../index.html";
    brand.textContent = "YASAR";
    const small = document.createElement("small");
    small.textContent = config.kind || "interactive demo";
    brand.appendChild(small);
    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = config.caption || "safe local simulation";
    const nav = document.createElement("nav");
    if (config.repo) {
      const repo = document.createElement("a");
      repo.href = config.repo;
      repo.target = "_blank";
      repo.rel = "noreferrer";
      repo.textContent = "View source ↗";
      nav.appendChild(repo);
    }
    if (config.sourceDoc) {
      const doc = document.createElement("a");
      doc.href = config.sourceDoc;
      doc.textContent = "README ↗";
      nav.appendChild(doc);
    }
    header.append(brand, tag, nav);
    document.body.prepend(header);
  }
  if (config.title) document.title = config.title;
  document.querySelectorAll("[data-demo-year]").forEach(node => { node.textContent = new Date().getFullYear(); });
  document.querySelectorAll("[data-demo-repo]").forEach(node => {
    if (config.repo) { node.href = config.repo; node.hidden = false; }
  });
  document.querySelectorAll("[data-demo-doc]").forEach(node => {
    if (config.sourceDoc) { node.href = config.sourceDoc; node.hidden = false; }
  });
})();