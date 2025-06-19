document.querySelectorAll(".info span").forEach(span => {
  // Adiciona um título de ajuda
  span.title = "Clique para copiar";

  // Muda o cursor ao passar o mouse
  span.style.cursor = "pointer";

  // Armazena o conteúdo original para restaurar depois
  span.dataset.original = span.innerText;

  // Evento de clique
  span.addEventListener("click", () => {
    navigator.clipboard.writeText(span.innerText).then(() => {
      span.innerText = "Copiado!";
      span.style.color = "#9b59b6"; // muda cor temporariamente

      setTimeout(() => {
        span.innerText = span.dataset.original;
        span.style.color = ""; // volta à cor padrão
      }, 1200);
    });
  });
});
