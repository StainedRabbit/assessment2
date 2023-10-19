var modal = new bootstrap.Modal(document.getElementById("modal"));

// htmx.on("htmx:beforeSwap", (e) => {
//     // Empty response should stop the swap
//     if (!e.detail.xhr.response) {
//       e.detail.shouldSwap = false
//     }
//   })


htmx.on("modal-show", function (event) {
    modal.show();
  });

htmx.on("modal-hide", function (event) {
modal.hide();
});
