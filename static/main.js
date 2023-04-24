document.addEventListener("DOMContentLoaded", () => {
  const generatePostButton = document.getElementById("generate_post_button");
  const postSubjectInput = document.getElementById("post_subject");
  const generatedPostTextArea = document.getElementById("generated_post");
  const publishPostButton = document.getElementById("publish_post_button");
  const previewPostButton = document.getElementById("preview_post_button");

  // Add this line to set the enctype attribute for the generated post form
  generatedPostTextArea.form.setAttribute("enctype", "multipart/form-data");

  async function generatePost() {
    const response = await fetch("/generate_post", {
      method: "POST",
      body: new FormData(postSubjectInput.form),
    });
  
    const responseText = await response.text(); // Add this line
    console.log("Raw response text:", responseText); // Add this line
  
    const data = JSON.parse(responseText); // Change this line
    generatedPostTextArea.value = data.generated_post;
  
    generatedPostTextArea.form.setAttribute("enctype", "multipart/form-data"); // Add this line
  }  

  function previewPost() {
    const postPreviewContainer = document.getElementById(
      "post_preview_container"
    );

    postPreviewContainer.innerHTML = "";
    postPreviewContainer.innerHTML = generatedPostTextArea.value;
  }

  async function publishPost() {
    const formData = new FormData(generatedPostTextArea.form);
    formData.append("content", generatedPostTextArea.value); // Add this line
  
    const requestOptions = {
      method: "POST",
      body: formData, // Change this line
    };
  
    try {
      const response = await fetch("/publish_post", requestOptions);
  
      if (response.ok) {
        alert("Post published successfully.");
      } else {
        const errorText = await response.text();
        alert(`Error publishing post: ${errorText}`);
      }
    } catch (error) {
      console.error("Error in publishPost:", error);
    }
  }    
  

  generatePostButton.addEventListener("click", (event) => {
    event.preventDefault();
    generatePost();
  });
  publishPostButton.addEventListener("click", (event) => {
    event.preventDefault(); // Add this line
    publishPost();
  });  
  previewPostButton.addEventListener("click", previewPost);
});
