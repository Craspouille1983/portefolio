const filterButtons = document.querySelectorAll('.filter-button');
const projects = document.querySelectorAll('.project .project-bottom');

filterButtons[0].classList.add('active');
for (let i = 0; i < projects.length; i++) {
	projects[i].closest('.project').setAttribute('style', `--i: ${i / projects.length}s`)
}
function filterProjects(filterValue) {
  projects.forEach(project => {
    project.closest('.project').classList.add('is-filtering'); 
    setTimeout(_ => {
      project.closest('.project').classList.remove('is-filtering');
      // project.closest('.project').classList.toggle('filter', !project.classList.contains(filterValue));
    }, 500);
    setTimeout(_ => {
      project.closest('.project').classList.toggle('filter', !project.classList.contains(filterValue));
    }, 600);
  });
}

filterButtons.forEach(button => {
  button.addEventListener('click', function() {
    const filterValue = this.dataset.filter.toLowerCase();
    filterButtons.forEach(button => button.classList.toggle('active', button === this));
    filterProjects(filterValue);
  });
});