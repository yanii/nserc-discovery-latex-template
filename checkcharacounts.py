#!/usr/bin/env python3

import subprocess
import sys

files_counts = {
    'most_significant_contributions.tex': 9000,
    'hqp_training_plan.tex': 9000,
    'additional_information_contributions.tex': 3000,
    'summary_of_proposal.tex': 3000,
    'relationship_to_other_funding': 12000,
    'past_contributions_to_hqp': 6000,
    'dnd_relevance': 3000,
}

files_pages = {
    'budget_justification.tex': 2,
    'proposal.tex': 5,
    'proposal_references.tex': 2,
}

return_status = 0

for file, max_count in files_counts.items():
    output = subprocess.run([f'detex {file} | wc -m'], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    count = int(output)
    # assert count <= int(max_count)
    if count > int(max_count):
        print(f'WARNING: file {file} has {count} > {max_count} characters!')
        return_status=1
    else:
        print(f'file {file} has {count} <= {max_count} characters.')

sys.exit(return_status)
