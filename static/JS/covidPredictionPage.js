var previewImage = document.getElementById('previewImage');
var imageInput = document.getElementById('uploadImageInput');

function readImageSource(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      previewImage.setAttribute('src', e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

function checkforImage() {
  if (imageInput.files[0]) {
    console.log('Aahe Image');
    console.log(imageInput.files);
    console.log(imageInput.files[0]);
    return true;
  }
  console.log('Konhe Image');
  return false;
}