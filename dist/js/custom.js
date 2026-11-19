document.querySelectorAll('#mainMenu a[href^="#"]').forEach((link) => {
  link.addEventListener('click', () => {
    const panel = document.getElementById('mainMenu');
    if (window.bootstrap) bootstrap.Offcanvas.getInstance(panel)?.hide();
  });
});
