---
layout: page
title: Projects
subtitle: My GitHub repositories and open source contributions
---

<div class="projects-container">

## Featured Projects

<div class="project-card" id="project-1">
<h3><a href="https://github.com/skthetester/amazon-price-tracker" target="_blank">🛒 Amazon Price Tracker</a></h3>
<div class="project-meta">
<span class="badge badge-python">Python</span>
<span class="project-date">Created: September 2025</span>
</div>
<div class="project-readme" id="readme-amazon-price-tracker">
<p><em>Loading README content...</em></p>
</div>
</div>

<div class="project-card" id="project-2">
<h3><a href="https://github.com/skthetester/Whitby-Bylaws-AI" target="_blank">🏛️ Whitby Bylaws AI</a></h3>
<div class="project-meta">
<span class="badge badge-python">Python</span>
<span class="project-stars">⭐ 1</span>
</div>
<div class="project-readme" id="readme-Whitby-Bylaws-AI">
<p><em>Loading README content...</em></p>
</div>
</div>

</div>

<style>
.projects-container {
  max-width: 100%;
  margin: 0 auto;
}

.project-card {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 25px;
  margin-bottom: 35px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s ease;
}

.project-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.project-card h3 {
  margin-top: 0;
  margin-bottom: 10px;
  color: #007bff;
  border-bottom: 2px solid #007bff;
  padding-bottom: 10px;
}

.project-card h3 a {
  text-decoration: none;
  color: inherit;
}

.project-card h3 a:hover {
  text-decoration: underline;
}

.project-meta {
  margin-bottom: 15px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8em;
  font-weight: bold;
  text-transform: uppercase;
}

.badge-python {
  background: #3776ab;
  color: white;
}

.badge-java {
  background: #f89820;
  color: white;
}

.project-stars {
  color: #ffa500;
  font-size: 0.9em;
}

.project-date, .project-type {
  color: #666;
  font-size: 0.9em;
}

.project-readme {
  margin-top: 15px;
  background: white;
  padding: 20px;
  border-radius: 6px;
  border-left: 4px solid #007bff;
  max-height: 400px;
  overflow-y: auto;
}

.project-readme h1 {
  color: #333;
  font-size: 1.5em;
  margin-bottom: 15px;
}

.project-readme h2 {
  color: #444;
  font-size: 1.3em;
  margin-top: 20px;
  margin-bottom: 10px;
}

.project-readme h3 {
  color: #555;
  font-size: 1.1em;
  margin-top: 15px;
  margin-bottom: 8px;
}

.project-readme pre {
  background: #f6f8fa;
  padding: 15px;
  border-radius: 6px;
  overflow-x: auto;
  border: 1px solid #e1e4e8;
}

.project-readme code {
  background: #f6f8fa;
  padding: 2px 4px;
  border-radius: 3px;
  font-size: 0.9em;
  color: #e83e8c;
}

.project-readme pre code {
  background: none;
  padding: 0;
  color: inherit;
}

.project-readme a {
  color: #007bff;
  text-decoration: none;
}

.project-readme a:hover {
  text-decoration: underline;
}

.project-readme ul, .project-readme ol {
  padding-left: 20px;
}

.project-readme blockquote {
  border-left: 4px solid #dfe2e5;
  padding-left: 15px;
  margin-left: 0;
  color: #666;
  font-style: italic;
}

@media (max-width: 768px) {
  .project-card {
    padding: 15px;
  }
  
  .project-readme {
    padding: 15px;
  }
}
</style>

<script>
// Function to fetch and display README content from GitHub
async function fetchREADME(username, repoName, containerId) {
  try {
    const response = await fetch(`https://api.github.com/repos/${username}/${repoName}/readme`);
    if (!response.ok) {
      throw new Error('README not found');
    }
    
    const data = await response.json();
    const readmeContent = atob(data.content);
    
    // Enhanced markdown to HTML conversion
    let htmlContent = readmeContent
      // Headers
      .replace(/^### (.*$)/gim, '<h3>$1</h3>')
      .replace(/^## (.*$)/gim, '<h2>$1</h2>')
      .replace(/^# (.*$)/gim, '<h1>$1</h1>')
      // Bold and italic
      .replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      // Code blocks and inline code
      .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
      .replace(/`(.*?)`/g, '<code>$1</code>')
      // Links
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>')
      // Lists
      .replace(/^\* (.*$)/gim, '<li>$1</li>')
      .replace(/^- (.*$)/gim, '<li>$1</li>')
      // Blockquotes
      .replace(/^> (.*$)/gim, '<blockquote>$1</blockquote>')
      // Line breaks
      .replace(/\n\n/g, '</p><p>')
      .replace(/\n/g, '<br>');
    
    // Wrap in paragraphs
    htmlContent = '<p>' + htmlContent + '</p>';
    
    // Clean up list formatting
    htmlContent = htmlContent.replace(/<\/p><p><li>/g, '<ul><li>');
    htmlContent = htmlContent.replace(/<\/li><br><\/p>/g, '</li></ul>');
    htmlContent = htmlContent.replace(/<li>(.*?)<br>/g, '<li>$1</li>');
    
    document.getElementById(containerId).innerHTML = htmlContent;
  } catch (error) {
    console.error(`Error fetching README for ${repoName}:`, error);
    document.getElementById(containerId).innerHTML = 
      `<p><em>Could not load README content. <a href="https://github.com/${username}/${repoName}" target="_blank">View repository on GitHub</a></em></p>`;
  }
}

// Load README content when page loads
document.addEventListener('DOMContentLoaded', function() {
  // Fetch README content for each repository
  fetchREADME('skthetester', 'amazon-price-tracker', 'readme-amazon-price-tracker');
  fetchREADME('skthetester', 'Whitby-Bylaws-AI', 'readme-Whitby-Bylaws-AI');
  fetchREADME('testingchief', 'linkedin-quotes', 'readme-linkedin-quotes');
  fetchREADME('skthetester', 'applitools-hackathon', 'readme-applitools-hackathon');
  fetchREADME('skthetester', 'python-project-template', 'readme-python-project-template');
});
</script>
