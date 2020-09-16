// /*  ==========================================
//     SHOW UPLOADED IMAGE
// * ========================================== */

// $(document).ready(function () {
//   function readURL() {
//     const input = $("#upload");
//     if (input.files && input.files[0]) {
//       var reader = new FileReader();

//       reader.onload = function (e) {
//         $("#imageResult").attr("src", e.target.result);
//       };
//       reader.readAsDataURL(input.files[0]);
//     }
//   }

//   function postData() {
//     const input = $("#upload");
//     console.log(input.files);
//     let formData = new FormData();
//     formData.append("image", input.files[0]);
//     $.ajax({
//       method: "POST",
//       url: "demo-cmt/",
//       data: formData,
//       contentType: "multipart/form-data",
//       success: function (data) {
//         console.log(data);
//       },
//     });
//   }

//   $("#upload").on("change", function () {
//     readURL(input);
//     postData();
//   });

//   /*  ==========================================
//     SHOW UPLOADED IMAGE NAME
// * ========================================== */
//   var input = document.getElementById("upload"); //$("#upload");
//   var infoArea = $("#upload-label");

//   input.addEventListener("change", showFileName);
//   function showFileName(event) {
//     var input = event.srcElement;
//     var fileName = input.files[0].name;
//     infoArea.textContent = "File name: " + fileName;
//   }
// });

/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */

function postData(input) {
  let formData = new FormData();
  formData.append("image", input.files[0]);
  console.log(input.files);
  //   $.ajax({
  //     method: "POST",
  //     url: "demo-cmt/",
  //     data: formData,
  //     contentType: "multipart/form-data",
  //     success: function (data) {
  //       console.log(data);
  //     },
  //   });
  $.ajax({
    url: "demo-cmt/",
    type: "post",
    data: formData,
    contentType: false,
    processData: false,
    success: function (response) {
      console.log(response);
    },
  });
}

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $("#imageResult").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

$(function () {
  $("#upload").on("change", function () {
    readURL(input);
    postData(input);
  });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById("upload");
var infoArea = document.getElementById("upload-label");

input.addEventListener("change", showFileName);
function showFileName(event) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  infoArea.textContent = "File name: " + fileName;
}
