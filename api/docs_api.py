from flask import Blueprint, jsonify, render_template_string, request

docs_bp = Blueprint("docs_bp", __name__)


OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "Clinic Metrics API",
        "version": "1.0.0",
        "description": "API for listing, creating, fetching, and deleting call metrics.",
    },
    "servers": [
        {
            "url": "https://clinicmetrics-backend.onrender.com",
        }
    ],
    "paths": {
        "/api/call-metrics": {
            "get": {
                "summary": "List all call metrics",
                "responses": {
                    "200": {
                        "description": "A list of call metrics",
                    }
                },
            },
            "post": {
                "summary": "Create a call metric",
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object"
                            }
                        }
                    },
                },
                "responses": {
                    "201": {
                        "description": "Call metric created",
                    },
                    "400": {
                        "description": "Invalid request body",
                    },
                },
            },
        },
        "/api/call-metrics/{call_id}": {
            "get": {
                "summary": "Get one call metric",
                "parameters": [
                    {
                        "name": "call_id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                        },
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Call metric found",
                    },
                    "404": {
                        "description": "Call metric not found",
                    },
                },
            },
            "delete": {
                "summary": "Delete a call metric",
                "parameters": [
                    {
                        "name": "call_id",
                        "in": "path",
                        "required": True,
                        "schema": {
                            "type": "integer",
                        },
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Call metric deleted",
                    },
                    "404": {
                        "description": "Call metric not found",
                    },
                },
            },
        },
    },
}


@docs_bp.route("/openapi.json", methods=["GET"])
def openapi_json():
    return jsonify(OPENAPI_SPEC)


@docs_bp.route("/docs", methods=["GET"])
def docs():
    spec_url = request.url_root.rstrip("/") + "/openapi.json"
    html = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Clinic Metrics API Docs</title>
    <style>
      :root {
        --bg: #f4f7fb;
        --panel: rgba(255, 255, 255, 0.96);
        --line: #d9e2f1;
        --text: #16233a;
        --muted: #61708d;
        --blue: #2d66f6;
        --green: #00a56b;
        --red: #e32e2e;
        --dark: #101a33;
      }
      body {
        margin: 0;
        background: var(--bg);
        color: var(--text);
        font-family: Arial, sans-serif;
      }
      .page {
        max-width: 1320px;
        margin: 0 auto;
        padding: 40px 24px 64px;
      }
      .hero,
      .panel {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 28px;
        box-shadow: 0 18px 45px rgba(31, 48, 83, 0.08);
      }
      .hero {
        padding: 32px 36px;
        margin-bottom: 24px;
      }
      .eyebrow {
        margin: 0 0 10px;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 0.12em;
        color: #6e7f9e;
      }
      h1, h2, h3, p {
        margin: 0;
      }
      h1 {
        font-size: 44px;
        line-height: 1.05;
        margin-bottom: 14px;
      }
      .subtext {
        font-size: 18px;
        line-height: 1.6;
        color: var(--muted);
        max-width: 1100px;
      }
      .grid {
        display: grid;
        grid-template-columns: 1.05fr 0.95fr;
        gap: 22px;
      }
      .panel {
        padding: 24px;
      }
      .panel h2 {
        font-size: 28px;
        margin-bottom: 18px;
      }
      .endpoint-list {
        display: grid;
        gap: 14px;
      }
      .endpoint {
        display: grid;
        grid-template-columns: 92px 1fr auto;
        gap: 18px;
        align-items: center;
        border: 1px solid #dce5f2;
        border-radius: 18px;
        padding: 18px;
        background: #fff;
      }
      .badge {
        border: 0;
        border-radius: 999px;
        color: #fff;
        font-weight: 800;
        font-size: 15px;
        padding: 12px 18px;
        cursor: pointer;
      }
      .badge.get { background: var(--blue); }
      .badge.post { background: var(--green); }
      .badge.delete { background: var(--red); }
      .endpoint-path {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 4px;
      }
      .endpoint-desc {
        color: #697a96;
        font-size: 15px;
      }
      .actions {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
      }
      .action-btn {
        border: 1px solid #cfd8e8;
        background: #fff;
        color: #183153;
        border-radius: 999px;
        padding: 10px 14px;
        font-size: 14px;
        font-weight: 700;
        cursor: pointer;
      }
      .action-btn.primary {
        background: #183153;
        color: #fff;
        border-color: #183153;
      }
      .spec-box {
        background: var(--dark);
        border-radius: 20px;
        padding: 18px;
        color: #e8f0ff;
        min-height: 420px;
        overflow: auto;
        white-space: pre-wrap;
        font-size: 13px;
        line-height: 1.65;
      }
      .small {
        color: var(--muted);
        font-size: 14px;
        margin: 10px 0 14px;
      }
      .result {
        margin-top: 14px;
        padding: 14px;
        border-radius: 14px;
        background: #eef4ff;
        border: 1px solid #cad8ff;
        font-size: 14px;
        color: #17315b;
      }
      @media (max-width: 960px) {
        h1 { font-size: 34px; }
        .grid { grid-template-columns: 1fr; }
        .endpoint { grid-template-columns: 1fr; }
      }
    </style>
  </head>
  <body>
    <div class="page">
      <section class="hero">
        <p class="eyebrow">CLINIC METRICS API</p>
        <h1>API Documentation</h1>
        <p class="subtext">
          This backend powers the dashboard and serves call metrics from the connected database.
          Use the buttons below to open the live endpoint, copy URLs, or jump to the OpenAPI spec.
        </p>
      </section>

      <section class="grid">
        <div class="panel">
          <h2>Endpoints</h2>
          <div class="endpoint-list">
            <div class="endpoint">
              <button class="badge get" data-method="GET" data-url="/api/call-metrics">GET</button>
              <div>
                <div class="endpoint-path"><code>/api/call-metrics</code></div>
                <div class="endpoint-desc">List all call metrics.</div>
              </div>
              <div class="actions">
                <button class="action-btn primary" data-open="/api/call-metrics">Open</button>
                <button class="action-btn" data-copy="/api/call-metrics">Copy URL</button>
              </div>
            </div>

            <div class="endpoint">
              <button class="badge post" data-method="POST" data-url="/api/call-metrics">POST</button>
              <div>
                <div class="endpoint-path"><code>/api/call-metrics</code></div>
                <div class="endpoint-desc">Create a new call metric record.</div>
              </div>
              <div class="actions">
                <button class="action-btn primary" data-open="/openapi.json">Spec</button>
                <button class="action-btn" data-copy="/api/call-metrics">Copy URL</button>
              </div>
            </div>

            <div class="endpoint">
              <button class="badge delete" data-method="DELETE" data-url="/api/call-metrics/&lt;call_id&gt;">DELETE</button>
              <div>
                <div class="endpoint-path"><code>/api/call-metrics/&lt;call_id&gt;</code></div>
                <div class="endpoint-desc">Delete a call metric by call ID.</div>
              </div>
              <div class="actions">
                <button class="action-btn primary" data-open="/openapi.json">Spec</button>
                <button class="action-btn" data-copy="/api/call-metrics/&lt;call_id&gt;">Copy URL</button>
              </div>
            </div>
          </div>
          <div class="result" id="action-result">Click any button to open the endpoint or copy its URL.</div>
        </div>

        <div class="panel">
          <h2>OpenAPI</h2>
          <p class="small">You can fetch the schema as JSON.</p>
          <div class="actions" style="margin-bottom: 12px;">
            <button class="action-btn primary" data-open="/openapi.json">Open OpenAPI JSON</button>
            <button class="action-btn" data-copy="/openapi.json">Copy spec URL</button>
            <button class="action-btn" data-open="/docs/swagger">Open Swagger UI</button>
          </div>
          <pre class="spec-box" id="spec-box">Loading...</pre>
        </div>
      </section>
    </div>

    <script>
      const specUrl = "{{ spec_url }}";
      const resultBox = document.getElementById("action-result");
      const specBox = document.getElementById("spec-box");

      async function loadSpec() {
        try {
          const response = await fetch(specUrl, { headers: { "Accept": "application/json" } });
          const json = await response.json();
          specBox.textContent = JSON.stringify(json, null, 2);
        } catch (error) {
          specBox.textContent = "Unable to load OpenAPI JSON.";
        }
      }

      async function copyToClipboard(text) {
        await navigator.clipboard.writeText(text);
        resultBox.textContent = "Copied: " + text;
      }

      function openPath(path) {
        window.open(path, "_blank", "noopener,noreferrer");
        resultBox.textContent = "Opened: " + path;
      }

      document.addEventListener("click", async (event) => {
        const openButton = event.target.closest("[data-open]");
        const copyButton = event.target.closest("[data-copy]");
        const badge = event.target.closest("[data-method]");

        if (openButton) {
          openPath(openButton.dataset.open);
        }

        if (copyButton) {
          const text = copyButton.dataset.copy;
          try {
            await copyToClipboard(text);
          } catch (error) {
            resultBox.textContent = "Copy failed. URL: " + text;
          }
        }

        if (badge) {
          const method = badge.dataset.method;
          const url = badge.dataset.url;
          if (method === "GET") {
            openPath(url);
          } else if (method === "POST") {
            resultBox.textContent = "POST uses JSON body. Open the OpenAPI JSON for the schema.";
          } else if (method === "DELETE") {
            resultBox.textContent = "DELETE needs a numeric call_id in the URL path.";
          }
        }
      });

      window.onload = loadSpec;
    </script>
  </body>
</html>
"""
    return render_template_string(html, spec_url=spec_url)


@docs_bp.route("/docs/swagger", methods=["GET"])
def swagger_ui():
    spec_url = request.url_root.rstrip("/") + "/openapi.json"
    html = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Clinic Metrics Swagger UI</title>
    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css" />
    <style>
      body {
        margin: 0;
        background: #f4f7fb;
        font-family: Arial, sans-serif;
      }
      #swagger-ui {
        max-width: 1400px;
        margin: 0 auto;
      }
    </style>
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-standalone-preset.js"></script>
    <script>
      window.onload = () => {
        SwaggerUIBundle({
          url: "{{ spec_url }}",
          dom_id: "#swagger-ui",
          deepLinking: true,
          presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
          layout: "BaseLayout",
        });
      };
    </script>
  </body>
</html>
"""
    return render_template_string(html, spec_url=spec_url)
