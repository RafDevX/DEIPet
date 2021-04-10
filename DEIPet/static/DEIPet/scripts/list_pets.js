/* Logic to allow changing page size without form submission */

document.getElementById("pageSizeSelect").addEventListener("change", (e) => {
	window.location.href =
		e.target.options[e.target.selectedIndex].dataset.newUrl;
});
