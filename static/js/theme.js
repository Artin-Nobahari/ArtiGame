const html = document.documentElement;

const icons = {
  system: document.getElementById("system-icon"),
  dark: document.getElementById("moon-icon"),
  light: document.getElementById("sun-icon"),
};

function setTheme(theme) {
  const appliedTheme =
    theme === "system"
      ? window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light"
      : theme;

  localStorage.setItem("theme", theme);
  html.dataset.theme = appliedTheme;

  Object.entries(icons).forEach(([name, icon]) => {
    icon.classList.toggle("hidden", name !== theme);
  });
}

document.querySelectorAll("[data-theme-value]").forEach((button) => {
  button.addEventListener("click", () => {
    setTheme(button.dataset.themeValue);
  });
});

setTheme(localStorage.getItem("theme") || "system");