# Continuous Machine Learning

Als Data-Science-Team wollen wir so oft wie möglich zusammenarbeiten und unsere Arbeit integrieren. Um sicherzustellen, dass unsere Arbeit nicht nur lokal durchgeführt wird ("aber es funktioniert auf meinem Rechner") und mit der Arbeit der anderen kompatibel ist, möchten wir unsere Daten- und Trainingspipeline als Teil unserer kontinuierlichen Integrationspipeline (CI) ausführen.
In diesem Showcase möchten wir zeigen, wie Sie eine einfache CI-Pipeline einrichten können, die über Github Actions läuft und das Modell für jede gepushte Commit-Gruppe trainiert. Als nettes Bonus-Feature werden wir cml.dev verwenden, um Trainingsmetriken an eine Pull-Anfrage zu senden.
Haftungsausschluss
Dieser Showcase basiert auf dem offiziellen [cml.dev](cml.dev)-Implementierungsbeispiel :)