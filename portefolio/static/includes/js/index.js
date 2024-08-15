const lists = document.querySelectorAll(".filter-button, span[data-filter]");
const items = document.querySelectorAll(".project .project-bottom");
let sizeX = "380";
let sizeY = "190";

for (let i = 0; i < items.length; i++) {
  items[i]
    .closest(".project")
    .setAttribute("style", `--i: ${i / items.length}s`);
}

lists.forEach((list) => {
  list.addEventListener("click", function () {
    let value = this.dataset.filter.toLowerCase();
    if (!this.classList.contains("active")) {
      items.forEach((item) => {
        for (let i = 0; i < lists.length; i++) {
          lists[i].classList.remove("active");
        }
        if (item.classList.contains(`${value}`)) {
          setTimeout((_) => {
            item.closest(".project").classList.remove("filter");
          }, 600);
          setTimeout((_) => {
            item.closest(".project").style.width = `${sizeX}px`;
            item.closest(".project").style.height = `${sizeY}px`;
          }, 800);
        }
        if (!item.classList.contains(`${value}`)) {
          setTimeout((_) => {
            item.closest(".project").style.width = "0";
            item.closest(".project").style.height = "0";
          }, 600);
          setTimeout((_) => {
            item.closest(".project").classList.add("filter");
          }, 800);
        }
      });
      this.classList.add("active");
    } else {
      items.forEach((item) => {
        this.classList.remove("active");
        setTimeout((_) => {
          item.closest(".project").style.width = `${sizeX}px`;
          item.closest(".project").style.height = `${sizeY}px`;
        }, 600);
        item.closest(".project").classList.remove("filter");
      });
    }
  });
});
