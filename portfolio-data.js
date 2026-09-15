/* Edit this file to update portfolio copy, links, and project metadata.
   "repo" is the direct public source repository. "demo" is a relative, offline
   browser demonstration hosted in the demos/ directory. */
window.PORTFOLIO = {
  brand: { name: "YASAR", descriptor: "SOFTWARE SYSTEMS ENGINEERING", short: "YSSE" },
  contact: { github: "https://github.com/Yasar101", email: "mailto:yasarashraf@outlook.com" },
  projects: [
    {
      name: "CLI Calculator",
      category: "Software development",
      type: "INTERACTIVE_DEMO",
      tech: "Python · Decimal",
      status: "Tested",
      repo: "https://github.com/Yasar101/python-cli-calculator",
      demo: "demos/calculator.html",
      focus: "Safe arithmetic parsing and explicit validation",
      limitation: "Command-line demonstration only; small three-token grammar.",
      command: "python3 -m projects.cli_calculator.calculator \"12.5 * 4\""
    },
    {
      name: "Expense Tracker",
      category: "Software development",
      type: "INTERACTIVE_DEMO",
      tech: "Python · JSON",
      status: "Tested",
      repo: "https://github.com/Yasar101/personal-expense-tracker",
      demo: "demos/expense-tracker.html",
      focus: "Expense models, totals and inspectable local persistence",
      limitation: "Persistent local CLI / browser-local demo; no server.",
      command: "python3 -m projects.expense_tracker --file expenses.json list"
    },
    {
      name: "Task Manager",
      category: "Software development",
      type: "INTERACTIVE_DEMO",
      tech: "Python · SQLite",
      status: "Tested",
      repo: "https://github.com/Yasar101/task-manager-application",
      demo: "demos/task-manager.html",
      focus: "Task lifecycle, filtering and local SQLite repository",
      limitation: "Persistent local CLI / browser-local demo; no web server.",
      command: "python3 -m projects.task_manager --database tasks.sqlite3 list --status open"
    },
    {
      name: "Energy Calculator Pro",
      category: "Software development",
      type: "INTERACTIVE_DEMO",
      tech: "Python · Decimal",
      status: "Tested",
      repo: "https://github.com/Yasar101/energy-calculator-pro",
      demo: "demos/energy-calculator.html",
      focus: "Transparent energy estimates using exact decimal calculations",
      limitation: "Estimate from supplied values; no live tariff or supplier integration.",
      command: "python3 -m projects.energy_calculator --watts 850 --hours 3.5 --days 30 --tariff 0.28"
    },
    {
      name: "Weather Dashboard",
      category: "Backend engineering",
      type: "SIMULATION",
      tech: "Python · HTTP adapter",
      status: "Tested core",
      repo: "https://github.com/Yasar101/weather-dashboard",
      demo: "demos/weather-dashboard.html",
      focus: "Provider-response validation separated from presentation",
      limitation: "Offline fixture demo; live command needs network access.",
      command: "python3 -m projects.weather_dashboard 51.5072 -0.1276"
    },
    {
      name: "PostgreSQL REST API",
      category: "Backend engineering",
      type: "INTERACTIVE_DEMO",
      tech: "Python · REST · SQL",
      status: "Tested reference",
      repo: "https://github.com/Yasar101/postgresql-rest-api",
      demo: "demos/rest-api.html",
      focus: "HTTP semantics, validation and replaceable repository boundary",
      limitation: "Reference implementation; PostgreSQL adapter is not connected in this demo.",
      command: "python3 demo.py api"
    },
    {
      name: "Real-Time Monitoring Dashboard",
      category: "Systems engineering",
      type: "ANIMATED_DEMO",
      tech: "Python · bounded metrics",
      status: "Tested core",
      repo: "https://github.com/Yasar101/real-time-monitoring-dashboard",
      demo: "demos/monitoring-dashboard.html",
      focus: "Thread-safe bounded metric windows and health states",
      limitation: "Simulated telemetry only; no live monitoring source is attached.",
      command: "python3 -m projects.monitoring_dashboard latency_ms 112 128 146 121 --threshold 130"
    },
    {
      name: "Microservices Commerce Platform",
      category: "Systems engineering",
      type: "ARCHITECTURE_DEMO",
      tech: "Python · workflows",
      status: "Tested core",
      repo: "https://github.com/Yasar101/microservices-commerce-platform",
      demo: "demos/commerce.html",
      focus: "Inventory reservation and payment-failure compensation",
      limitation: "Fictional in-process transactions; not deployed services.",
      command: "python3 -m projects.microservices_commerce --decline-payment"
    },
    {
      name: "AI Developer Assistant",
      category: "AI engineering",
      type: "SIMULATION",
      tech: "Python · retrieval boundary",
      status: "Tested core",
      repo: "https://github.com/Yasar101/ai-developer-assistant",
      demo: "demos/assistant.html",
      focus: "Context retrieval, provider abstraction and credential rejection",
      limitation: "Local deterministic provider; no external model or API key.",
      command: "python3 -m projects.ai_developer_assistant \"Where is token refresh handled?\""
    },
    {
      name: "Distributed AI Systems Platform",
      category: "Software architecture",
      type: "SIMULATION",
      tech: "Python · leases · retries",
      status: "Tested core",
      repo: "https://github.com/Yasar101/distributed-ai-systems-platform",
      demo: "demos/scheduler.html",
      focus: "Worker ownership, expiring leases and bounded retries",
      limitation: "In-process scheduler with simulated workers, not deployed infrastructure.",
      command: "python3 -m projects.distributed_ai_platform --fail"
    },
    {
      name: "HTML & CSS Foundations",
      category: "Front-end web",
      type: "LIVE_PAGE",
      tech: "HTML5 · CSS3",
      status: "Validated",
      repo: "https://github.com/Yasar101/html-css-foundations",
      demo: "demos/html-css-foundations/index.html",
      focus: "Semantic structure, accessible styling, responsive one-pager",
      limitation: "Static single page; no JavaScript or server behavior.",
      command: "python3 -m http.server 8000"
    },
    {
      name: "Responsive Web Foundations",
      category: "Front-end web",
      type: "LIVE_PAGE",
      tech: "HTML5 · CSS Grid · Flexbox",
      status: "Validated",
      repo: "https://github.com/Yasar101/responsive-web-foundations",
      demo: "demos/responsive-web-foundations/index.html",
      focus: "Mobile-first layouts, fluid type and accessible navigation",
      limitation: "Static single page; resizing exercises the breakpoints.",
      command: "python3 -m http.server 8000"
    },
    {
      name: "PHP Calculator Fundamentals",
      category: "Server-side web",
      type: "INTERACTIVE_DEMO",
      tech: "PHP · forms · validation",
      status: "Linted + tested",
      repo: "https://github.com/Yasar101/php-calculator-fundamentals",
      demo: "demos/php-calculator.html",
      focus: "Server-side form handling, escaping and arithmetic",
      limitation: "Browser simulation; the real page requires a PHP runtime.",
      command: "php -S localhost:8000"
    },
    {
      name: "Fitness Tracking Web App",
      category: "Full-stack web",
      type: "LIVE_PAGE",
      tech: "HTML · CSS · JS · Node · MySQL",
      status: "Validated",
      repo: "https://github.com/Yasar101/fitness-tracking-web-app",
      demo: "demos/fitness-tracker/index.html",
      focus: "Responsive workout log with browser-local persistence",
      limitation: "Workouts stay in the browser; registration needs a configured database.",
      command: "npm install && npm start"
    },
    {
      name: "PHP Project Management System",
      category: "Full-stack web",
      type: "ARCHITECTURE_DEMO",
      tech: "PHP · MySQL (PDO)",
      status: "Linted + tested",
      repo: "https://github.com/Yasar101/php-project-management-system",
      demo: "demos/project-manager.html",
      focus: "Authentication, ownership-based authorization and CRUD workflows",
      limitation: "Architecture visualization and simulated list; needs PHP+MySQL to run fully.",
      command: "php project-manager-php/tests/ValidationTest.php"
    }
  ]
};