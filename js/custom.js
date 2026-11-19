document.querySelectorAll('#mainMenu a[href^="#"]').forEach((link) => {
  link.addEventListener('click', () => {
    const panel = document.getElementById('mainMenu');
    if (window.bootstrap) bootstrap.Offcanvas.getInstance(panel)?.hide();
  });
});

// Keep the original image link usable when dialogs are unavailable.
const figureLinks = document.querySelectorAll('.figure-open');
if (figureLinks.length && typeof HTMLDialogElement !== 'undefined') {
  const dialog = document.createElement('dialog');
  dialog.className = 'figure-dialog';
  dialog.setAttribute('aria-labelledby', 'figure-dialog-title');
  dialog.innerHTML = '<div class="figure-dialog-header"><h2 id="figure-dialog-title"></h2><div class="figure-dialog-actions"><a target="_blank" rel="noopener">Full resolution ↗</a><button class="figure-dialog-close" type="button" aria-label="Close figure">×</button></div></div><img class="figure-dialog-image" alt="">';
  document.body.append(dialog);
  const fullImage = dialog.querySelector('img');
  const heading = dialog.querySelector('h2');
  const fullLink = dialog.querySelector('a');
  figureLinks.forEach(link => {
    link.setAttribute('aria-haspopup', 'dialog');
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      fullImage.src = link.href;
      fullImage.alt = link.querySelector('img').alt;
      heading.textContent = link.dataset.figureTitle;
      fullLink.href = link.href;
      dialog.showModal();
      document.body.classList.add('figure-viewing');
    });
  });
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => document.body.classList.remove('figure-viewing'));
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
}
