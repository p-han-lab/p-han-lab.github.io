document.querySelectorAll('#mainMenu a[href^="#"]').forEach((link) => {
  link.addEventListener('click', () => {
    const panel = document.getElementById('mainMenu');
    if (window.bootstrap) bootstrap.Offcanvas.getInstance(panel)?.hide();
  });
});

// Addresses are maintained in each member's data-email attribute in people.html.
// Both the portrait and name control the same accessible disclosure.
document.querySelectorAll('[data-email-toggle]').forEach((button) => {
  button.addEventListener('click', () => {
    const member = button.closest('.member');
    const panel = document.getElementById(button.getAttribute('aria-controls'));
    if (!member || !panel) return;
    const expand = panel.hidden;
    if (expand) {
      const address = (member.dataset.email || '').trim();
      if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(address)) {
        const link = document.createElement('a');
        link.href = 'mailto:' + address;
        link.textContent = address;
        panel.replaceChildren(link);
      } else {
        panel.textContent = 'Email to be added.';
      }
    }
    panel.hidden = !expand;
    member.querySelectorAll('[data-email-toggle]').forEach((control) => {
      control.setAttribute('aria-expanded', String(expand));
    });
  });
});
