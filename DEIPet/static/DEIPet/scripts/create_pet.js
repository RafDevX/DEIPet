/* Logic for making the create pet form more user friendly */

do {
	/* new block just for scope */
	const div = document.getElementById("petImageUrlsFakeInputs");
	const textarea = document.getElementById("petImageUrlsRealInput");
	const inputs = [];

	for (const line of textarea.value.split("\n")) {
		if (line) {
			addInput().value = line;
		}
	}

	function addInput() {
		const cont = document.createElement("div");
		cont.className = "form-floating mb-3";
		const inp = document.createElement("input");
		inp.type = "url";
		inp.className = "form-control";
		inp.placeholder = "https://example.com";
		inp.required = true;
		const label = document.createElement("label");
		label.innerText = "URL";
		cont.appendChild(inp);
		cont.appendChild(label);
		div.appendChild(cont);
		inputs.push({ container: cont, input: inp });
		return inp;
	}
} while (false);
