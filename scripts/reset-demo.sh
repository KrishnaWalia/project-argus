#!/usr/bin/env bash
# Resets all state and reloads the fixed demo dataset (sample-data/) so the live pitch
# always starts from a known-clean state. Run this before every rehearsal AND right before
# you actually present — never demo on top of leftover state from a previous test run.
#
# Owner: Database role (persistence layer), with Backend role wiring the load-fixture
# endpoint this script calls. Fill in the real commands once those pieces exist.

set -e

echo "1. Clearing Neo4j..."
# TODO(database role): MATCH (n) DETACH DELETE n  (via cypher-shell or the neo4j driver)

echo "2. Clearing Postgres demo tables..."
# TODO(database role): TRUNCATE the relevant tables (not audit_log — see security role)

echo "3. Loading sample-data/ fixtures..."
# TODO(backend role): POST sample-data/documents.json, evidence.json, actor-nodes.json
# to the backend's load-fixture endpoint (or call a seed script directly)

echo "Demo reset complete. Verify with: curl http://localhost:8000/api/v1/actor-nodes"
