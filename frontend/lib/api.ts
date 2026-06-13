export async function generateProject(requirements: string) {
  const response = await fetch("http://localhost:8000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ requirements }),
  });

  if (!response.ok) {
    throw new Error("Failed to generate project");
  }

  return response.json();
}