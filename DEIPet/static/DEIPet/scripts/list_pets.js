/* Logic to allow changing page size without form submission */

"use strict";

document.getElementById("pageSizeSelect").addEventListener("change", (e) => {
	window.location.href =
		e.target.options[e.target.selectedIndex].dataset.newUrl;
});
