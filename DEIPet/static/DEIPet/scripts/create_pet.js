/* Logic for making the create pet form more user friendly */

"use strict";

document.addEventListener("DOMContentLoaded", () => {
	const form = document.getElementById("createPetForm");
	const container = document.getElementById("petImageUrlsContainer");
	const textarea = document.getElementById("petImageUrlsRealInput");
	const submitBtn = document.getElementById("createPetSubmitBtn");

	const addPetImageBtn = document.getElementById("addPetImageBtn");
	const addPetImageModal = new bootstrap.Modal(
		document.getElementById("addPetImageModal")
	);
	const addPetImageUrl = document.getElementById("addPetImageUrl");
	const addPetImageSubmitBtn = document.getElementById(
		"addPetImageSubmitBtn"
	);
	const addPetImageFile = document.getElementById("addPetImageFile");

	const actual_images = [];
	const tooltips = [];
	let busy = true;

	window.onbeforeunload = () => true;

	const images = new Proxy(actual_images, {
		deleteProperty: function (target, prop) {
			delete target[prop];
			updateForm();
			return true;
		},
		set: function (target, prop, val) {
			target[prop] = val;
			updateForm();
			return true;
		},
	});

	for (let line of textarea.value.split("\n")) {
		tryAddImage(line);
	}
	rebuildContainer();
	busy = false;

	function tryAddImage(url) {
		try {
			url = url.trim();
			if (url && (url = new URL(url)) && url.protocol != "javascript:") {
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
		if (images.length) {
			for (let i = 0; i < images.length; i++) {
				await createCard(i);
			}
		} else {
			const p = document.createElement("p");
			p.className = "text-muted fst-italic w-100 m-3";
			p.innerText =
				"Por favor adicione pelo menos duas imagens usando o botão abaixo.";
			container.appendChild(p);
		}
	}

	async function createCard(i) {
		const col = document.createElement("div");
		col.className = "col-auto d-flex align-items-stretch";
		const card = document.createElement("div");
		card.className = "card m-3 shadow";
		const img = document.createElement("img");
		img.src = images[i];
		img.className = "card-img-top";
		img.alt = `#${i + 1}`;
		const body = document.createElement("div");
		body.className = "card-body d-flex";
		const btngroup = document.createElement("div");
		btngroup.className = "btn-group highlight-middle-btn mt-auto mx-auto";
		btngroup.role = "group";
		for (let j = 0; j < 4; j++) {
			const btn = document.createElement("button");
			btn.type = "button";
			btn.className =
				"btn btn-outline-" +
				[
					"secondary" + (i == 0 ? " disabled" : ""),
					"primary" + (i == 0 ? " disabled" : ""),
					"danger",
					"secondary" + (i + 1 == images.length ? " disabled" : ""),
				][j];
			btn.innerText = ["❰", "★", "✖", "❱"][j];
			btn.title = {
				"❰": "Para a Esquerda",
				"★": "Definir como Principal",
				"✖": "Apagar Imagem",
				"❱": "Para a Direita",
			}[btn.innerText];
			tooltips.push(new bootstrap.Tooltip(btn));
			btn.addEventListener(
				"click",
				async () => {
					if (busy) return;
					busy = true;
					await {
						"❰": async () =>
							([images[i], images[i - 1]] = [
								images[i - 1],
								images[i],
							]),
						"★": async () => images.unshift(images.splice(i, 1)[0]),
						"✖": async () => images.splice(i, 1),
						"❱": async () =>
							([images[i], images[i + 1]] = [
								images[i + 1],
								images[i],
							]),
					}[btn.innerText]();
					await rebuildContainer();
					busy = false;
				},
				{ passive: true, once: true }
			);
			btngroup.appendChild(btn);
		}
		body.appendChild(btngroup);
		card.appendChild(img);
		card.appendChild(body);
		col.appendChild(card);
		container.appendChild(col);
	}

	function updateForm() {
		textarea.value = images.join("\n");
		textarea.setCustomValidity(
			images.length < 2 ? "São necessárias pelo menos duas imagens!" : ""
		);
		submitBtn.disabled = !form.checkValidity();
	}

	function btnFeedback(btn, txt, cls, middleCallback) {
		const initialTxt = btn.innerText;
		const initialDis = btn.disabled;
		btn.disabled = true;
		btn.classList.add(cls);
		btn.classList.remove("btn-primary");
		btn.innerText = txt;
		setTimeout(() => {
			if (middleCallback) middleCallback();
			setTimeout(() => {
				btn.classList.add("btn-primary");
				btn.classList.remove(cls);
				btn.innerText = initialTxt;
				btn.disabled = initialDis;
			}, 500);
		}, 500);
	}

	form.addEventListener("submit", () => {
		window.onbeforeunload = null;
	});

	addPetImageBtn.addEventListener("click", () => {
		addPetImageModal.show();
	});

	addPetImageUrl.addEventListener("input", () => {
		addPetImageSubmitBtn.disabled = !addPetImageUrl.checkValidity();
	});

	addPetImageSubmitBtn.addEventListener("click", () => {
		if (tryAddImage(addPetImageUrl.value)) {
			rebuildContainer();
			addPetImageUrl.value = "";
			addPetImageSubmitBtn.disabled = true;
			btnFeedback(
				addPetImageSubmitBtn,
				"Adicionado!",
				"btn-success",
				() => addPetImageModal.hide()
			);
		} else {
			btnFeedback(addPetImageSubmitBtn, "Inválido!", "btn-danger");
		}
	});

	addPetImageFile.addEventListener("change", () => {
		addPetImageFile.classList.remove("text-danger");
		if (addPetImageFile.files.length) {
			const file = addPetImageFile.files[0];
			if (file.type.match(/^image\/.+$/) && file.size <= 1e6) {
				const reader = new FileReader();
				reader.addEventListener("load", () => {
					if (tryAddImage(reader.result)) {
						rebuildContainer();
						addPetImageFile.classList.add("text-success");
						setTimeout(() => {
							addPetImageModal.hide();
							addPetImageFile.value = null;
							addPetImageFile.classList.remove("text-success");
						}, 500);
					} else {
						addPetImageFile.classList.add("text-danger");
					}
				});
				reader.readAsDataURL(file);
			} else {
				addPetImageFile.classList.add("text-danger");
			}
		}
	});
});
