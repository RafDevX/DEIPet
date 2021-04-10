/* General client-side handling */

for (const el of document.querySelectorAll(".fake-anchor")) {
	el.addEventListener(
		"click",
		() => (window.location.href = el.dataset.faHref)
	);
}
