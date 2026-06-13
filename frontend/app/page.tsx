"use client";

import { useState } from "react";
import { generateProject } from "@/lib/api";
import OutputTabs from "./components/OutputTabs";

export default function Home() {
  const [requirements, setRequirements] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    if (!requirements.trim()) {
      setError("Requirements දාන්න!");
      return;
    }
    setError("");
    setLoading(true);
    setResult(null);

    try {
      const data = await generateProject(requirements);
      setResult(data);
    } catch (err) {
      setError("Something went wrong. Backend running ද check කරන්න.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 py-10 px-4">
      <div className="max-w-4xl mx-auto">

        {/* Header */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-extrabold text-blue-700">
            🤖 AI Software Development Team
          </h1>
          <p className="text-gray-500 mt-2">
            Describe your project → AI agents build it end-to-end
          </p>
        </div>

        {/* Input */}
        <div className="bg-white rounded-2xl shadow p-8 space-y-6">
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1">
              Project Requirements
            </label>
            <textarea
              value={requirements}
              onChange={(e) => setRequirements(e.target.value)}
              placeholder="e.g. Build a TODO app with user authentication, where users can create, edit, delete tasks and mark them complete..."
              rows={6}
              className="w-full border border-gray-300 rounded-xl px-4 py-3 text-sm text-gray-900 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {error && <p className="text-red-500 text-sm">{error}</p>}

          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-blue-600 text-white py-3 rounded-xl font-semibold hover:bg-blue-700 disabled:opacity-50 transition"
          >
            {loading ? "AI Team is working... ⏳ (1-2 min)" : "Build My Project 🚀"}
          </button>
        </div>

        {/* Output */}
        {result && <OutputTabs result={result} />}
      </div>
    </main>
  );
}