'use strict';
const form = document.querySelector('#registration-form');
const status = document.querySelector('#registration-status');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const password = form.elements.password.value;
  const confirmation = document.querySelector('#password-confirmation');
  confirmation.setCustomValidity(password === confirmation.value ? '' : 'Passwords do not match.');
  if (!form.reportValidity()) return;
  status.className = 'status'; status.textContent = 'Creating account…';
  try {
    const response = await fetch('/api/register', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name: form.elements.name.value, email: form.elements.email.value, password }) });
    const result = await response.json();
    if (!response.ok) throw new Error((result.errors ?? ['Registration failed.']).join(' '));
    status.className = 'status success'; status.textContent = result.message; form.reset();
  } catch (error) {
    status.className = 'status error'; status.textContent = error.message === 'Failed to fetch' ? 'The registration server is not available.' : error.message;
  }
});
