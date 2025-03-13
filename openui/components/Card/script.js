document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("button").forEach(btn => {
      btn.addEventListener("click", () => {
        console.log(`[Button] clicked: ${btn.id || btn.textContent}`);
      });
    });
  });
  