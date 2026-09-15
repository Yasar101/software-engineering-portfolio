(() => {
  const { brand, contact, projects } = window.PORTFOLIO;
  const grid = document.querySelector("#projects");
  const filter = document.querySelector("#filter");
  const categories = [...new Set(projects.map(({ category }) => category))];
  categories.forEach(category => filter.add(new Option(category, category)));
  const escape = value => String(value).replace(/[&<>'"]/g, char => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;","\"":"&quot;"}[char]));
  const render = () => {
    const selected = filter.value;
    const items = selected === "All" ? projects : projects.filter(item => item.category === selected);
    grid.innerHTML = items.map((item, index) => `<article class="project"><div class="project-top"><span class="index">${String(index + 1).padStart(2, "0")}</span><span class="type">${escape(item.type.replace("_", " "))}</span></div><h3>${escape(item.name)}</h3><p class="focus">${escape(item.focus)}</p><p class="tech">${escape(item.tech)} <b>${escape(item.status)}</b></p><details><summary>Demo and limitations</summary><p>${escape(item.limitation)}</p><code>${escape(item.command)}</code><button class="copy" type="button" data-command="${escape(item.command)}">Copy command</button></details><div class="links"><a href="${escape(item.repo)}" target="_blank" rel="noreferrer">Repository ↗</a>${item.live ? `<a href="${escape(item.live)}" target="_blank" rel="noreferrer">Live demo ↗</a>` : ""}</div></article>`).join("");
  };
  render(); filter.addEventListener("change", render);
  document.addEventListener("click", event => { const button = event.target.closest(".copy"); if (button && navigator.clipboard) { navigator.clipboard.writeText(button.dataset.command); button.textContent = "Copied"; setTimeout(() => button.textContent = "Copy command", 1200); } });
  document.querySelectorAll("[data-contact]").forEach(link => { link.href = contact[link.dataset.contact]; });
  document.querySelector("#year").textContent = new Date().getFullYear();
  const theme = document.querySelector("#theme"); const stored = localStorage.getItem("ysse-theme"); if (stored) document.documentElement.dataset.theme = stored;
  theme.addEventListener("click", () => { const next = document.documentElement.dataset.theme === "light" ? "dark" : "light"; document.documentElement.dataset.theme = next; localStorage.setItem("ysse-theme", next); });
})();
