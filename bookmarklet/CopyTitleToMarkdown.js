javascript: (function () {
  input = document.createElement('input');
  input.value = `[${document.title}](${location.href})`;
  document.body.appendChild(input);
  input.select();
  document.execCommand('Copy');
  document.body.removeChild(input)
})();