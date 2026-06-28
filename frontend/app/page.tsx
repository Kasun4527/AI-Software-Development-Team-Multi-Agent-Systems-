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
      setError("Please enter your project requirements.");
      return;
    }
    setError("");
    setLoading(true);
    setResult(null);

    try {
      const data = await generateProject(requirements);
      setResult(data);
    } catch (err) {
      setError("Something went wrong. Please check that the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="relative min-h-screen overflow-hidden bg-slate-950 py-16 px-4 text-slate-100">
      {/* Ambient background glows */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -left-32 h-96 w-96 rounded-full bg-blue-600/30 blur-3xl" />
        <div className="absolute top-1/3 -right-32 h-96 w-96 rounded-full bg-fuchsia-600/20 blur-3xl" />
        <div className="absolute bottom-0 left-1/3 h-96 w-96 rounded-full bg-cyan-500/20 blur-3xl" />
      </div>

      <div className="relative z-10 mx-auto max-w-4xl">
        {/* Header */}
        <div className="mb-12 text-center">
          <span className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-1.5 text-xs font-medium text-slate-300 backdrop-blur">
            <span className="h-2 w-2 animate-pulse rounded-full bg-emerald-400" />
            Powered by autonomous AI agents
          </span>
          <h1 className="mt-6 bg-gradient-to-r from-blue-400 via-indigo-300 to-fuchsia-400 bg-clip-text text-5xl font-extrabold tracking-tight text-transparent">
            AI Software Development Team
          </h1>
          <p className="mx-auto mt-4 max-w-xl text-base text-slate-400">
            Describe your project and let a team of AI agents build it
            end-to-end — from architecture to working code.
          </p>
        </div>

        {/* Input card */}
        <div className="rounded-3xl border border-white/10 bg-white/5 p-8 shadow-2xl shadow-black/40 backdrop-blur-xl">
          <div className="space-y-6">
            <div>
              <label className="mb-2 block text-sm font-semibold text-slate-200">
                Project Requirements
              </label>
              <textarea
                value={requirements}
                onChange={(e) => setRequirements(e.target.value)}
                placeholder="e.g. Build a TODO app with user authentication, where users can create, edit, delete tasks and mark them complete..."
                rows={6}
                className="w-full resize-none rounded-2xl border border-white/10 bg-slate-900/60 px-4 py-3 text-sm text-slate-100 placeholder:text-slate-500 transition focus:border-blue-400/50 focus:outline-none focus:ring-2 focus:ring-blue-500/40"
              />
            </div>

            {error && (
              <div className="flex items-center gap-2 rounded-xl border border-red-500/20 bg-red-500/10 px-4 py-3 text-sm text-red-300">
                <span>⚠️</span>
                {error}
              </div>
            )}

            <button
              onClick={handleSubmit}
              disabled={loading}
              className="group relative w-full overflow-hidden rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 py-3.5 text-sm font-semibold text-white shadow-lg shadow-blue-900/40 transition hover:from-blue-500 hover:to-indigo-500 disabled:cursor-not-allowed disabled:opacity-60"
            >
              <span className="relative z-10 flex items-center justify-center gap-2">
                {loading ? (
                  <>
                    <span className="h-4 w-4 animate-spin rounded-full border-2 border-white/30 border-t-white" />
                    AI team is working… (1–2 min)
                  </>
                ) : (
                  <>Build My Project 🚀</>
                )}
              </span>
            </button>
          </div>
        </div>

        {/* Output */}
        {result && (
          <div className="mt-8">
            <OutputTabs result={result} />
          </div>
        )}
      </div>
    </main>
  );
}