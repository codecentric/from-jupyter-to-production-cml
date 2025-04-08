# Dagster + CML MLOps Template 🤖🔬🛠️

This repository is a minimal example of how to integrate [CML (Continuous Machine Learning)](https://cml.dev) and 
[Dagster](https://dagster.io) into your MLOps workflow. 
It uses GitHub Actions to orchestrate and automate a simple machine learning pipeline with reporting directly on your pull requests. 🚀🔁

## Introduction 📄🚀

This project demonstrates how to implement a CI/CD pipeline using GitHub Actions that:
- Executes a [Dagster](https://dagster.io) job to train and evaluate a machine learning model (Random Forest).
- Uses [CML](https://cml.dev) to report metrics (e.g., accuracy) back to GitHub via PR comments.

By combining these tools, you get a reproducible, automated, and collaborative machine learning workflow in a fully
Git-based environment. 🧪🛠️📊

## What's Inside 🧬📁

- **Dagster Pipeline**: A simple ML job defined in Python using Dagster to:
  - Load and split the Iris dataset.
  - Train a `RandomForestClassifier`.
  - Evaluate the model’s accuracy.
  
- **GitHub Actions Workflow**: A CI/CD pipeline in `.github/workflows/pipeline.yml` that:
  - Sets up Python.
  - Installs dependencies.
  - Executes the Dagster job via CLI.
  - Logs accuracy to a file.
  - Posts a comment on the PR using CML.

## Getting Started 🛠️🏁

To get this template running in your own repo:

1. **Create a new repository using this template**:
   - Click “Use this template” at the top right.
   - Name your new repository.

2. **Clone your new repo locally**:
   ```bash
   git clone https://github.com/yourusername/your-mlops-repo.git
   cd your-mlops-repo
   ```

3. **Customize and test your workflow**:
   - The GitHub Actions workflow is already set to trigger on `pull_request` with the `main` branch as a target.
   - You can manually trigger it by creating or updating a pull request with main as the target branch.

4. **View the results**:
   - Once the CI job completes, CML will post an accuracy score as a comment on the PR.
   - This ensures quick visibility into model performance without switching tools.

## CML Reporting 📢📊

CML is used to post model evaluation results back to GitHub. Here's how it's done:

- During the GitHub Actions run, the Dagster job writes model accuracy to a `metrics.txt` file.
- CML reads this file and posts the contents as a PR comment using:
  ```bash
  cml comment create --file metrics.txt
  ```

You can expand on this by:
- Adding plots (e.g., confusion matrix).
- Tracking experiments with DVC or MLFlow.
- Exporting models or data as artifacts.

More info in the [CML Docs](https://docs.cml.dev).

## License 📜

This project is licensed under the [MIT License](LICENSE). Use, modify, and share freely!

## Acknowledgments 🙏

- Huge thanks to the CML and Dagster communities.
- Inspiration from MLOps best practices and real-world workflows.
