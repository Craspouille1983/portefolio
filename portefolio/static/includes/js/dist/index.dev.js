"use strict";

var lists = document.querySelectorAll(".filter-button");
var items = document.querySelectorAll(".project .project-bottom");
var sizeX = "340";
var sizeY = "190";

for (var i = 0; i < items.length; i++) {
  items[i].closest(".project").setAttribute("style", "--i: ".concat(i / items.length, "s"));
}

lists.forEach(function (list) {
  list.addEventListener("click", function () {
    var _this = this;

    var value = this.dataset.filter.toLowerCase();

    if (!this.classList.contains("active")) {
      items.forEach(function (item) {
        for (var _i = 0; _i < lists.length; _i++) {
          lists[_i].classList.remove("active");
        }

        if (item.classList.contains("".concat(value))) {
          setTimeout(function (_) {
            item.closest(".project").classList.remove("filter");
          }, 600);
          setTimeout(function (_) {
            item.closest(".project").style.width = "".concat(sizeX, "px");
            item.closest(".project").style.height = "".concat(sizeY, "px");
          }, 800);
        }

        if (!item.classList.contains("".concat(value))) {
          setTimeout(function (_) {
            item.closest(".project").style.width = "0";
            item.closest(".project").style.height = "0";
          }, 600);
          setTimeout(function (_) {
            item.closest(".project").classList.add("filter");
          }, 800);
        }
      });
      this.classList.add("active");
    } else {
      items.forEach(function (item) {
        _this.classList.remove("active");

        setTimeout(function (_) {
          item.closest(".project").style.width = "".concat(sizeX, "px");
          item.closest(".project").style.height = "".concat(sizeY, "px");
        }, 600);
        item.closest(".project").classList.remove("filter");
      });
    }
  });
});