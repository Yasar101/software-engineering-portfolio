'use strict';
const form = document.querySelector('#workout-form');
const list = document.querySelector('#workout-list');
const emptyMessage = document.querySelector('#empty-workouts');
const status = document.querySelector('#workout-status');
const clearButton = document.querySelector('#clear-workouts');
const storageKey = 'aston-fitness-workouts';

function readWorkouts() {
  try { return JSON.parse(localStorage.getItem(storageKey)) ?? []; } catch { return []; }
}
function writeWorkouts(workouts) { localStorage.setItem(storageKey, JSON.stringify(workouts)); }
function renderWorkouts() {
  const workouts = readWorkouts();
  list.replaceChildren();
  emptyMessage.hidden = workouts.length > 0;
  clearButton.hidden = workouts.length === 0;
  workouts.slice(0, 10).forEach((workout) => {
    const item = document.createElement('li');
    const title = document.createElement('strong');
    const details = document.createElement('span');
    title.textContent = workout.activity;
    details.textContent = `${workout.duration} min · ${workout.effort} effort · ${workout.date}`;
    item.append(title, details); list.append(item);
  });
}
form.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  const workout = { activity: data.get('activity'), duration: Number(data.get('duration')), effort: data.get('effort'), date: new Date().toLocaleDateString() };
  writeWorkouts([workout, ...readWorkouts()].slice(0, 50));
  form.reset(); status.textContent = 'Workout saved on this device.'; renderWorkouts();
});
clearButton.addEventListener('click', () => { localStorage.removeItem(storageKey); status.textContent = 'Workout history cleared.'; renderWorkouts(); });
renderWorkouts();
