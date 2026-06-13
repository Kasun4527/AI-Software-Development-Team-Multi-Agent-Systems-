"use client";

import { useState } from "react";

type Result = {
  project_plan: string;
  requirements_spec: string;
  backend_code: string;
  frontend_code: string;
  review_report: string;
  test_code: string;
};

const TABS = [
  { key: "project_plan", label: "📋 Project Plan" },
  { key: "requirements_spec", label: "📝 Requirements" },
  { key: "backend_code", label: "⚙️ Backend Code" },
  { key: "frontend_code", label: "🎨 Frontend Code" },
  { key: "review_report", label: "🔍 Code Review" },
  { key: "test_code", label: "🧪 Tests" },
] as const;

export default function OutputTabs({ result }: { result: Result }) {
  const [active, setActive] = useState<keyof Result>("project_plan");

  const copy = () => {
    navigator.clipboard.writeText(result[active]);
    alert("Copied!");
  };

  return (
    <div className="mt-8 bg-white rounded-2xl shadow overflow-hidden">
      {/* Tab buttons */}
      <div className="flex flex-wrap border-b border-gray-200 bg-gray-50">
        {TABS.map((tab) => (
          <button
            key={tab.key}
            onClick={() => setActive(tab.key)}
            className={`px-4 py-3 text-sm font-medium transition ${
              active === tab.key
                ? "bg-white text-blue-600 border-b-2 border-blue-600"
                : "text-gray-500 hover:text-gray-700"
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="p-6">
        <div className="flex justify-end mb-2">
          <button
            onClick={copy}
            className="bg-blue-600 text-white px-4 py-1 rounded-lg text-sm hover:bg-blue-700"
          >
            Copy
          </button>
        </div>
        <pre className="whitespace-pre-wrap text-sm text-gray-800 bg-gray-50 p-4 rounded-lg overflow-x-auto max-h-[500px] overflow-y-auto">
          {result[active]}
        </pre>
      </div>
    </div>
  );
}