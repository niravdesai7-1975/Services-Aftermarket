import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Services & Aftermarket AI Dashboard",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
    }
    
    .stPlotlyChart {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_services_aftermarket_data():
    """Load and prepare the services and aftermarket AI use case data"""
    
    use_cases = [
        'Field Service Management', 'Upselling during Service Visits', 'Troubleshooting assistant for field technicians',
        'Maintenance log', 'Route Optimizer', 'Connected Products', 'Asset Monitoring & Prognostics',
        'Churn Analytics', 'Stock Fill Ration Analytics', 'Social Listening and analytics',
        'Conversational AI chat bots', 'Facial Biometric Authentication', 'Customer Call Classification / Ticket routing',
        'Intelligent call routing', '24*7 support chatbots', 'Call Intent Discovery - Emotion AI',
        'Agent Response Suggestions', 'NLP based call / message analyser', 'Survey and Review Analytics',
        'Omnichannel Promotions', 'Lead generation and Acquisitions', 'Behavioural Pricing',
        'Personalised Offerings', 'Email Analyzer'
    ]
    
    sectors = [
        'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Industrial', 'Common', 'Automotive',
        'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common',
        'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common', 'Common'
    ]
    
    value_chains = [
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket',
        'Services and aftermarket', 'Services and aftermarket', 'Services and aftermarket'
    ]
    
    personas = [
        'Field Engineer', 'Field Engineer', 'Field Technician', 'Field Technician', 'Field Technician',
        'Service Engineer', 'Customers', 'Sales Engineer', 'Sales Engineer', 'Product Manager',
        'Service and support Engineer', 'Service and support Engineer', 'Service and support Engineer',
        'Service and support Engineer', 'End customer', 'Service and support Engineer',
        'Service and support Engineer', 'Product Manager', 'Marketing Department', 'Marketing Department',
        'Sales Manager', 'Sales Manager', 'Sales Manager', 'Service and support Engineer'
    ]
    
    descriptions = [
        'Auto generate service instructions',
        'Upselling capability during service visits',
        'Allow Field Technicians to search response from documents to support troubleshooting steps',
        'Allow field technicians to see past maintenance log of the elevators',
        'Using GenAI - redefine the Route Optimization',
        'Provide remote service operations to customer and consistent experience',
        'Predictive analytics-powered maintenance benefits car manufacturers as well as car owners. Customers get timely alerts about potential technical issues, and turn to manufacturers for maintenance rather than independent car repair shops.',
        'Get comprehensive view of the entire customer experience using AI based churn analytics.',
        'Get deeper insights in customer order fulfilment process and trigger automated actions to meet On time in full delivery commitments',
        'Collect, analyse and categorise voice of customer from social platforms and take informed decisions about product / service improvement',
        'Conversational AI coupled with RAG (Retrieval Augmented Generation) to support and resolve customer queries',
        'Verify customer to avoid fraudulent transactions using AI. Biometric identification is hard to break and hence enhanced security over critical data',
        'Identify the type of call and generate ticket for It',
        'Route Classified and tagged calls/ tickets to appropriate service desk',
        '24*7 Chatbots can answer queries by customer and log tickets. Escalations can be provided to emergency service providers (FIRE Service, Ambulance Service, Police Service etc)',
        'Identify the Intent of Customer and allocate right resources for quick resolution of concern using AI',
        'Based on conversation analysed by AI System , the agents are provided with guided diagnostic process which helps to address customer queries more accurately',
        'Customer Sentiment analysed based on NLP and actions are planned for product and service provisioning improvement',
        'AI system generating the surveys for the customer and collect feedback . The analysed reviews are summarised and presented in product listing page',
        'It unifies and analyzes data about customers and products to inform marketing campaigns, predict channels customers are more likely to convert on, and automate repetitive tasks.',
        'AI is used to automate and optimize various processes, including data analysis, lead scoring, and lead nurturing. By leveraging the power of AI, businesses can gain insights into their target audience, predict future behavior, and prioritize leads based on their potential value.',
        'Through machine learning, AI evaluates historical pricing data, market conditions, and customer responses to dynamically adjust prices. This automation enables you to implement pricing strategies that are responsive to real-time market trends and customer purchase patterns.',
        'AI personalization is helping to address the "choice overload" phenomena where individuals report lower choice satisfaction when faced with too many options.',
        'The customer sends an email, which is parsed by the LLM and gets directed to the concerned department in the organization for further analysis.'
    ]
    
    # Generate synthetic metrics for analysis
    business_impacts = [
        5, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
    ]
    
    implementation_complexities = [
        4, 3, 3, 2, 4, 5, 5, 4, 3, 3, 4, 4, 3, 3, 3, 4, 4, 3, 3, 4, 4, 4, 4, 3
    ]
    
    estimated_rois = [
        35.0, 25.0, 30.0, 20.0, 40.0, 45.0, 50.0, 35.0, 30.0, 35.0, 30.0, 40.0,
        25.0, 25.0, 20.0, 35.0, 30.0, 35.0, 30.0, 35.0, 40.0, 35.0, 30.0, 25.0
    ]
    
    implementation_timelines = [
        8, 5, 6, 4, 8, 10, 12, 8, 6, 6, 8, 8, 5, 5, 4, 8, 8, 6, 6, 8, 8, 8, 8, 5
    ]
    
    risk_levels = [
        'Medium', 'Low', 'Low', 'Low', 'Medium', 'High', 'High', 'Medium', 'Low', 'Low',
        'Medium', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Medium', 'Low', 'Low', 'Medium',
        'Medium', 'Medium', 'Medium', 'Low'
    ]
    
    # Create DataFrame
    df = pd.DataFrame({
        'use_case_name': use_cases,
        'sector': sectors,
        'value_chain': value_chains,
        'persona': personas,
        'description': descriptions,
        'business_impact': business_impacts,
        'implementation_complexity': implementation_complexities,
        'estimated_roi': estimated_rois,
        'implementation_timeline': implementation_timelines,
        'risk_level': risk_levels
    })
    
    # Calculate priority score (weighted combination of metrics)
    df['priority_score'] = (
        df['business_impact'] * 0.4 +
        (df['estimated_roi'] / 10) * 0.3 +
        (6 - df['implementation_complexity']) * 0.2 +
        df['risk_level'].map({'Low': 3, 'Medium': 2, 'High': 1}) * 0.1
    ).round(2)
    
    # Categorize priority levels
    df['priority_level'] = pd.cut(
        df['priority_score'],
        bins=[0, 3, 4, 5],
        labels=['Lower', 'Medium', 'High'],
        include_lowest=True
    )
    
    return df

def main():
    st.markdown('<h1 class="main-header">🔧 Services & Aftermarket AI Use Case Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_services_aftermarket_data()
    
    # Sidebar filters
    st.sidebar.header("📊 Filters")
    
    # Sector filter
    selected_sectors = st.sidebar.multiselect(
        "Select Sectors",
        options=df['sector'].unique(),
        default=df['sector'].unique()
    )
    
    # Priority level filter
    selected_priorities = st.sidebar.multiselect(
        "Select Priority Levels",
        options=df['priority_level'].unique(),
        default=df['priority_level'].unique()
    )
    
    # Risk level filter
    selected_risks = st.sidebar.multiselect(
        "Select Risk Levels",
        options=df['risk_level'].unique(),
        default=df['risk_level'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['sector'].isin(selected_sectors)) &
        (df['priority_level'].isin(selected_priorities)) &
        (df['risk_level'].isin(selected_risks))
    ]
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Use Cases", len(filtered_df))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_roi = filtered_df['estimated_roi'].mean()
        st.metric("Average ROI", f"{avg_roi:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_priority = filtered_df['priority_score'].mean()
        st.metric("Average Priority Score", f"{avg_priority:.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        high_priority = len(filtered_df[filtered_df['priority_level'] == 'High'])
        st.metric("High Priority Cases", high_priority)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Priority Distribution")
        priority_counts = filtered_df['priority_level'].value_counts()
        fig_priority = px.pie(
            values=priority_counts.values,
            names=priority_counts.index,
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
        )
        fig_priority.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig_priority, use_container_width=True)
    
    with col2:
        st.subheader("📈 ROI vs Implementation Timeline")
        fig_scatter = px.scatter(
            filtered_df,
            x='implementation_timeline',
            y='estimated_roi',
            color='priority_level',
            size='business_impact',
            hover_data=['use_case_name', 'sector'],
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
        )
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Sector Breakdown")
        sector_counts = filtered_df['sector'].value_counts()
        fig_sector = px.bar(
            x=sector_counts.index,
            y=sector_counts.values,
            color=sector_counts.values,
            color_continuous_scale='Viridis'
        )
        fig_sector.update_layout(height=400, xaxis_title="Sector", yaxis_title="Count")
        st.plotly_chart(fig_sector, use_container_width=True)
    
    with col2:
        st.subheader("⚠️ Risk Level Distribution")
        risk_counts = filtered_df['risk_level'].value_counts()
        fig_risk = px.bar(
            x=risk_counts.index,
            y=risk_counts.values,
            color=risk_counts.values,
            color_continuous_scale='Reds'
        )
        fig_risk.update_layout(height=400, xaxis_title="Risk Level", yaxis_title="Count")
        st.plotly_chart(fig_risk, use_container_width=True)
    
    # Top personas
    st.subheader("👥 Top 10 Personas by Use Case Count")
    persona_counts = filtered_df['persona'].value_counts().head(10)
    fig_persona = px.bar(
        x=persona_counts.values,
        y=persona_counts.index,
        orientation='h',
        color=persona_counts.values,
        color_continuous_scale='Blues'
    )
    fig_persona.update_layout(height=500, xaxis_title="Count", yaxis_title="Persona")
    st.plotly_chart(fig_persona, use_container_width=True)
    
    # Detailed use cases table
    st.markdown("---")
    st.subheader("📋 Detailed Use Cases")
    
    # Add search functionality
    search_term = st.text_input("🔍 Search use cases:", placeholder="Enter keywords...")
    
    if search_term:
        search_filtered = filtered_df[
            filtered_df['use_case_name'].str.contains(search_term, case=False) |
            filtered_df['description'].str.contains(search_term, case=False) |
            filtered_df['persona'].str.contains(search_term, case=False)
        ]
        display_df = search_filtered
    else:
        display_df = filtered_df
    
    # Sort options
    sort_by = st.selectbox(
        "Sort by:",
        ['Priority Score (High to Low)', 'Business Impact (High to Low)', 'ROI (High to Low)', 'Implementation Timeline (Low to High)']
    )
    
    if sort_by == 'Priority Score (High to Low)':
        display_df = display_df.sort_values('priority_score', ascending=False)
    elif sort_by == 'Business Impact (High to Low)':
        display_df = display_df.sort_values('business_impact', ascending=False)
    elif sort_by == 'ROI (High to Low)':
        display_df = display_df.sort_values('estimated_roi', ascending=False)
    elif sort_by == 'Implementation Timeline (Low to High)':
        display_df = display_df.sort_values('implementation_timeline', ascending=True)
    
    # Display the table
    st.dataframe(
        display_df[['use_case_name', 'sector', 'persona', 'priority_score', 'business_impact', 'estimated_roi', 'implementation_timeline', 'risk_level']],
        use_container_width=True,
        height=400
    )
    
    # Download button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name="services_aftermarket_ai_use_cases.csv",
        mime="text/csv"
    )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p><strong>Services & Aftermarket AI Use Case Dashboard</strong></p>
        <p>Comprehensive analysis of 24 AI use cases across service operations and aftermarket support</p>
        <p>Built with ❤️ using Streamlit and Python</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
