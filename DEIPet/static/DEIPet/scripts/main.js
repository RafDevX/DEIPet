/* General client-side handling */

"use strict";

for (const el of document.querySelectorAll(".fake-anchor")) {
	el.addEventListener(
		"click",
		() => (window.location.href = el.dataset.faHref)
	);
}

/* Enable bootstrap tooltips everywhere; as per docs */
[].slice
	.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
	.map((el) => {
		return new bootstrap.Tooltip(el);
	});
