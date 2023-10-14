document.addEventListener("DOMContentLoaded", function () {
  // Function to check if the browser supports WebP format
  function supportsWebP() {
    if (!self.createImageBitmap) return false;

    const image = new Image();
    image.src = "data:image/webp;base64,UklGRh4AAABXRUJQVlA4T4IAAAAeCQCdASo=";

    return image.decode().then(
      () => true,
      () => false
    );
  }

  // Function to convert an image source to WebP
  function convertToWebP(img) {
    const source = img.getAttribute("src");

    if (source && supportsWebP()) {
      const webPSource = source.replace(/\.(jpg|jpeg|png)/i, ".webp");
      img.setAttribute("src", webPSource);
    }
  }

  // Get all <img> elements and convert their sources to WebP
  const imgElements = document.querySelectorAll("img");
  imgElements.forEach(convertToWebP);
});
