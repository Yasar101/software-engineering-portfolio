(() => {
  const { brand, contact, projects } = window.PORTFOLIO;
  const grid = document.querySelector("#projects");
  const filter = document.querySelector("#filter");
  const categories = [...new Set(projects.map(({ category }) => category))];
  categories.forEach(category => filter.add(new Option(category, category)));
  const escape = value => String(value).replace(/[&<>'"]/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;","\"":"&quot;"}[char]));

  const typeLabel = type => type.replace(/_/g, " ");

  const render = () => {
    const selected = filter.value;
    const items = selected === "All" ? projects : projects.filter(item => item.category === selected);
    grid.innerHTML = items.map((item, index) => `
      <article class="project">
        <div class="project-top"><span class="index">${String(index + 1).padStart(2, "0")}</span><span class="type">${escape(typeLabel(item.type))}</span></div>
        <h3>${escape(item.name)}</h3>
        <p class="focus">${escape(item.focus)}</p>
        <p class="tech">${escape(item.tech)} <b>${escape(item.status)}</b></p>
        <details><summary>Demo and limitations</summary><p>${escape(item.limitation)}</p><code>${escape(item.command)}</code><button class="copy" type="button" data-command="${escape(item.command)}">Copy command</button></details>
        <div class="links">
          ${item.demo ? `<button class="demo" type="button" data-demo="${escape(item.demo)}">Try live demo</button>` : ""}
          <a href="${escape(item.repo)}" target="_blank" rel="noreferrer">View source ↗</a>
        </div>
      </article>`).join("");
  };

  const modal = document.querySelector("#demo-modal");
  const frame = document.querySelector("#demo-frame");
  const external = document.querySelector("#demo-external");
  const preventBodyScroll = locked => { document.body.style.overflow = locked ? "hidden" : ""; };
  const closeModal = () => { modal.hidden = true; frame.src = ""; external.href = "#"; preventBodyScroll(false); };

  document.addEventListener("click", event => {
    const button = event.target.closest(".copy");
    if (button && navigator.clipboard) { navigator.clipboard.writeText(button.dataset.command); button.textContent = "Copied"; setTimeout(() => button.textContent = "Copy command", 1200); return; }
    const demo = event.target.closest("[data-demo]");
    if (demo) {
      const src = demo.dataset.demo;
      external.href = src;
      frame.src = src;
      modal.hidden = false;
      document.querySelector("#demo-modal-title").textContent = demo.closest(".project").querySelector("h3").textContent + " — live demo";
      preventBodyScroll(true);
      return;
    }
    if (event.target.closest("[data-demo-close]")) closeModal();
  });
  document.addEventListener("keydown", event => { if (event.key === "Escape" && !modal.hidden) closeModal(); });

  render(); filter.addEventListener("change", render);
  document.querySelectorAll("[data-contact]").forEach(link => { link.href = contact[link.dataset.contact]; });
  document.querySelector("#year").textContent = new Date().getFullYear();
  const theme = document.querySelector("#theme");
  const stored = localStorage.getItem("ysse-theme");
  const apply = themeValue => { document.documentElement.dataset.theme = themeValue; theme.textContent = themeValue === "light" ? "◑" : "◐"; };
  apply(stored || "light");
  theme.addEventListener("click", () => { const next = document.documentElement.dataset.theme === "light" ? "dark" : "light"; apply(next); localStorage.setItem("ysse-theme", next); });
})();