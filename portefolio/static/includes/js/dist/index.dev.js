"use strict";

var filterButtons = document.querySelectorAll('.filter-button');
var projects = document.querySelectorAll('.project .project-bottom');
filterButtons[0].classList.add('active');

for (var i = 0; i < projects.length; i++) {
  projects[i].closest('.project').setAttribute('style', "--i: ".concat(i / projects.length, "s"));
}

function filterProjects(filterValue) {
  projects.forEach(function (project) {
    project.closest('.project').classList.add('is-filtering');
    setTimeout(function (_) {
      project.closest('.project').classList.remove('is-filtering'); // project.closest('.project').classList.toggle('filter', !project.classList.contains(filterValue));
    }, 500);
    setTimeout(function (_) {
      project.closest('.project').classList.toggle('filter', !project.classList.contains(filterValue));
    }, 600);
  });
}

filterButtons.forEach(function (button) {
  button.addEventListener('click', function () {
    var _this = this;

    var filterValue = this.dataset.filter.toLowerCase();
    filterButtons.forEach(function (button) {
      return button.classList.toggle('active', button === _this);
    });
    filterProjects(filterValue);
  });
});