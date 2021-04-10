/* Logic for making the create pet form more user friendly */

document.addEventListener("DOMContentLoaded", () => {
	const container = document.getElementById("petImageUrlsContainer");
	const textarea = document.getElementById("petImageUrlsRealInput");
	const images = [];
	const tooltips = [];
	let busy = true;

	for (let line of textarea.value.split("\n")) {
		tryAddImage(line);
	}
	rebuildContainer();
	busy = false;

	function tryAddImage(url) {
		try {
			url = url.trim();
			if (url && (url = new URL(url)) && url.protocol != "javascript") {
				images.push(url.href);
				return true;
			}
		} catch {}
		return false;
	}

	async function rebuildContainer() {
		let t;
		while ((t = tooltips.shift())) {
			await t.dispose();
		}
		container.textContent = "";
		for (let i = 0; i < images.length; i++) {
			const url = images[i];
			const col = document.createElement("div");
			col.className = "col-auto d-flex align-items-stretch";
			const card = document.createElement("div");
			card.className = "card m-3 shadow";
			const img = document.createElement("img");
			img.src = url;
			img.className = "card-img-top";
			img.alt = `#${i + 1}`;
			const body = document.createElement("div");
			body.className = "card-body";
			const btngroup = document.createElement("div");
			btngroup.className = "btn-group highlight-middle-btn";
			btngroup.role = "group";
			for (let j = 0; j < 3; j++) {
				const btn = document.createElement("button");
				btn.type = "button";
				btn.className =
					"btn btn-outline-" +
					[
						i > 0 ? "secondary" : "primary disabled",
						"danger",
						"secondary" +
							(i + 1 == images.length ? " disabled" : ""),
					][j];
				btn.innerText = [i > 0 ? "❰" : "★", "✖", "❱"][j];
				//btn.dataset.bsToggle = "tooltip";
				btn.title = {
					"★": "Imagem Principal",
					"❰": "Para a Esquerda",
					"✖": "Apagar Imagem",
					"❱": "Para a Direita",
				}[btn.innerText];
				tooltips.push(new bootstrap.Tooltip(btn, { trigger: "hover" }));
				if (btn.innerText != "★") {
					btn.addEventListener(
						"click",
						{
							"❰": async () => {
								if (busy) return;
								busy = true;
								[images[i], images[i - 1]] = [
									images[i - 1],
									images[i],
								];
								await rebuildContainer();
								busy = false;
							},
							"❱": async () => {
								if (busy) return;
								busy = true;
								[images[i], images[i + 1]] = [
									images[i + 1],
									images[i],
								];
								await rebuildContainer();
								busy = false;
							},
							"✖": async () => {
								if (busy) return;
								busy = true;
								images.splice(i, 1);
								await rebuildContainer();
								busy = false;
							},
						}[btn.innerText],
						{ passive: true, once: true }
					);
				}
				btngroup.appendChild(btn);
			}
			body.appendChild(btngroup);
			card.appendChild(img);
			card.appendChild(body);
			col.appendChild(card);
			container.appendChild(col);
		}
	}
});
