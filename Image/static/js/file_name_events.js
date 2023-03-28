const file = document.querySelector('.upload_file');
file.addEventListener('change', (e) => {
    // Get the selected file
    const [file] = e.target.files;
    // Get the file name and size
    const {name: fileName, size} = file;
    // Convert size in bytes to kilo bytes
    const fileSize = (size / 1000).toFixed(2);
    // Set the text content
    const fileNameAndSize = `${fileName.slice(-45)} - ${fileSize}KB`;
    document.querySelector('.file-name_1').textContent = fileNameAndSize;
});