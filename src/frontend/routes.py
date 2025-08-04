from flask import render_template, request, redirect, url_for, flash, session
from . import app
import os
import sys
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from automating_linkedin_profile_data_extraction_and_analysis.crew import AutomatingLinkedinProfileDataExtractionAndAnalysisCrew

@app.route('/', methods=['GET', 'POST'])
def index():
    steps = []
    profile_url = None
    if request.method == 'POST':
        linkedin_url = request.form.get('linkedin_url')
        profile_url = linkedin_url
        if not linkedin_url:
            flash('Please enter a LinkedIn profile URL.', 'danger')
            return redirect(url_for('index'))
        try:
            steps.append(f"Started scraping profile: {linkedin_url}")
            # Call the backend workflow with the LinkedIn URL
            inputs = {"linkedin_url": linkedin_url}
            crew = AutomatingLinkedinProfileDataExtractionAndAnalysisCrew().crew()
            
            # Execute the full workflow with inputs
            result = crew.kickoff(inputs=inputs)
            
            steps.append(f"Workflow completed successfully!")
            steps.append(f"Final result: {str(result)}")
            
            flash(f'Success! Profile data extracted successfully.', 'success')
            session['steps'] = steps
            session['profile_url'] = profile_url
            session['result'] = str(result)
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            session['steps'] = steps
            session['profile_url'] = profile_url
        return redirect(url_for('index'))
    steps = session.pop('steps', [])
    profile_url = session.pop('profile_url', None)
    result = session.pop('result', None)
    return render_template('index.html', steps=steps, profile_url=profile_url, result=result) 