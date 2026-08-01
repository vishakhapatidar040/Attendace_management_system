function confirmDelete(message) {
  return window.confirm(message);
}

document.addEventListener("DOMContentLoaded", () => {
  const splashScreen = document.getElementById("splashScreen");
  const animationsEnabled = document.documentElement.dataset.animations !== "off";

  if (splashScreen && animationsEnabled) {
    const splashSeen = sessionStorage.getItem("sam-splash-seen");
    if (!splashSeen) {
      document.body.classList.add("show-splash");
      sessionStorage.setItem("sam-splash-seen", "true");
      window.setTimeout(() => {
        splashScreen.classList.add("is-hidden");
        document.body.classList.remove("show-splash");
      }, 2200);
    } else {
      splashScreen.remove();
    }
  } else if (splashScreen) {
    splashScreen.remove();
  }

  const rows = document.querySelectorAll("tbody tr");
  rows.forEach((row, index) => {
    row.style.animationDelay = `${Math.min(index * 60, 360)}ms`;
  });

  const themeButtons = document.querySelectorAll("[data-theme-option]");
  const animationToggle = document.getElementById("animationToggle");
  const themeStatus = document.getElementById("themeStatus");
  const animationStatus = document.getElementById("animationStatus");
  const saveButton = document.getElementById("saveSettingsBtn");
  const resetButton = document.getElementById("resetSettingsBtn");

  const currentTheme = document.documentElement.dataset.theme || "system";
  const currentAnimations = document.documentElement.dataset.animations || "on";

  function applySettings(theme, animations) {
    document.documentElement.classList.add("theme-switching");
    document.documentElement.dataset.theme = theme;
    document.documentElement.dataset.animations = animations;
    localStorage.setItem("sam-theme", theme);
    localStorage.setItem("sam-animations", animations);
    if (themeStatus) {
      themeStatus.textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
    }
    if (animationStatus) {
      animationStatus.textContent = animations === "on" ? "On" : "Off";
    }
    if (animationToggle) {
      animationToggle.checked = animations === "on";
    }
    themeButtons.forEach((button) => {
      button.classList.toggle("active", button.dataset.themeOption === theme);
    });

    window.setTimeout(() => {
      document.documentElement.classList.remove("theme-switching");
    }, 420);
  }

  applySettings(currentTheme, currentAnimations);

  themeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      applySettings(button.dataset.themeOption, document.documentElement.dataset.animations || "on");
    });
  });

  if (animationToggle) {
    animationToggle.addEventListener("change", () => {
      document.documentElement.dataset.animations = animationToggle.checked ? "on" : "off";
      localStorage.setItem("sam-animations", document.documentElement.dataset.animations);
      if (animationStatus) {
        animationStatus.textContent = animationToggle.checked ? "On" : "Off";
      }
    });
  }

  if (saveButton) {
    saveButton.addEventListener("click", () => {
      const selectedTheme = document.documentElement.dataset.theme || "system";
      const selectedAnimations = document.documentElement.dataset.animations || "on";
      localStorage.setItem("sam-theme", selectedTheme);
      localStorage.setItem("sam-animations", selectedAnimations);
      if (themeStatus) {
        themeStatus.textContent = selectedTheme.charAt(0).toUpperCase() + selectedTheme.slice(1);
      }
      if (animationStatus) {
        animationStatus.textContent = selectedAnimations === "on" ? "On" : "Off";
      }
    });
  }

  if (resetButton) {
    resetButton.addEventListener("click", () => {
      applySettings("system", "on");
    });
  }
});