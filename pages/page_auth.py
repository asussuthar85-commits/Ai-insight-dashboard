"""
Dedicated Authentication Page
Enhanced login and signup with separate flows
"""

import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback
import dash
from core.config import NAVY, GOLD, PRIMARY_BG, CARD_BG, TEXT, TEXT_LIGHT, BORDER, PRIMARY


def generate_auth_page():
    """Generate a beautiful standalone authentication page"""
    
    return dbc.Container([
        dcc.Location(id='url-auth', refresh=False),
        
        dbc.Row([
            # Left Side - Branding & Features
            dbc.Col([
                html.Div([
                    # Logo
                    html.Div([
                        html.Div("◆", style={'fontSize': '56px', 'color': GOLD, 'marginBottom': '15px'}),
                        html.H1("ONEX AI", style={
                            'color': '#FFFFFF', 'fontWeight': '800', 
                            'marginBottom': '4px', 'fontSize': '42px', 'letterSpacing': '2px'
                        }),
                        html.P("Data Insight Platform", style={
                            'color': GOLD, 'fontSize': '16px', 'fontWeight': '600', 
                            'margin': '0', 'letterSpacing': '1px'
                        }),
                    ], style={'textAlign': 'center', 'marginBottom': '60px'}),
                    
                    # Features List
                    html.Div([
                        html.H3("Intelligent Analytics", style={
                            'color': '#FFFFFF', 'fontWeight': '700', 
                            'marginBottom': '24px', 'fontSize': '24px'
                        }),
                        *[
                            html.Div([
                                html.Div("✓", style={
                                    'color': GOLD, 'fontWeight': '800', 'fontSize': '20px',
                                    'marginRight': '16px', 'width': '24px'
                                }),
                                html.Div(feature, style={
                                    'color': TEXT_LIGHT, 'fontSize': '15px', 
                                    'fontWeight': '500', 'lineHeight': '1.6'
                                }),
                            ], style={'display': 'flex', 'alignItems': 'flex-start', 'marginBottom': '18px'})
                            for feature in [
                                "Auto-detect data patterns in seconds",
                                "Generate insightful dashboards automatically",
                                "Connect multiple data sources seamlessly",
                                "AI-powered insights and recommendations",
                                "Real-time data analysis and monitoring",
                            ]
                        ],
                    ], style={'marginTop': '40px'}),
                    
                ], style={
                    'backgroundColor': NAVY,
                    'padding': '60px 50px',
                    'minHeight': '100vh',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'justifyContent': 'center',
                    'color': '#FFFFFF',
                }),
            ], xs=12, md=6, style={'padding': '0'}),
            
            # Right Side - Form
            dbc.Col([
                html.Div([
                    # Tab Selection
                    dbc.Row([
                        dbc.Col([
                            html.Button(
                                "Sign In",
                                id='auth-btn-signin-tab',
                                n_clicks=1,
                                style={
                                    'background': 'none',
                                    'border': 'none',
                                    'fontSize': '18px',
                                    'fontWeight': '700',
                                    'color': NAVY,
                                    'cursor': 'pointer',
                                    'paddingBottom': '12px',
                                    'borderBottom': f'3px solid {NAVY}',
                                    'transition': 'all 0.3s ease',
                                }
                            ),
                        ], width=6),
                        dbc.Col([
                            html.Button(
                                "Create Account",
                                id='auth-btn-signup-tab',
                                n_clicks=0,
                                style={
                                    'background': 'none',
                                    'border': 'none',
                                    'fontSize': '18px',
                                    'fontWeight': '700',
                                    'color': TEXT_LIGHT,
                                    'cursor': 'pointer',
                                    'paddingBottom': '12px',
                                    'transition': 'all 0.3s ease',
                                }
                            ),
                        ], width=6),
                    ], style={
                        'borderBottom': f'2px solid {BORDER}', 
                        'marginBottom': '40px',
                        'paddingLeft': '0',
                        'paddingRight': '0',
                    }),
                    
                    # Sign In Form
                    html.Div(
                        id='auth-signin-form-container',
                        children=_get_signin_form(),
                        style={'display': 'block'}
                    ),

                    # Sign Up Form
                    html.Div(
                        id='auth-signup-form-container',
                        children=_get_signup_form(),
                        style={'display': 'none'}
                    ),
                    
                    # Error/Success Messages
                    html.Div(id='auth-message-container', style={'marginTop': '20px'}),
                    
                ], style={
                    'padding': '60px 40px',
                    'minHeight': '100vh',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'justifyContent': 'center',
                }),
            ], xs=12, md=6, style={'padding': '0', 'backgroundColor': PRIMARY_BG}),
        ], style={'margin': '0', 'height': '100vh'}),
        
    ], fluid=True, style={'padding': '0'})


def _get_signin_form():
    """Sign In form component"""
    return html.Div([
        # Email/Username
        html.Div([
            html.Label("Username or Email", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signin-username',
                type='text',
                placeholder='Enter your username or email',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                    'transition': 'border-color 0.3s ease',
                }
            ),
        ], style={'marginBottom': '20px'}),
        
        # Password
        html.Div([
            html.Label("Password", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signin-password',
                type='password',
                placeholder='Enter your password',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                    'transition': 'border-color 0.3s ease',
                }
            ),
        ], style={'marginBottom': '30px'}),
        
        # Sign In Button
        dbc.Button(
            "Sign In",
            id='auth-btn-signin',
            size='lg',
            style={
                'width': '100%',
                'backgroundColor': NAVY,
                'borderColor': NAVY,
                'color': '#FFFFFF',
                'fontWeight': '700',
                'fontSize': '15px',
                'padding': '12px 16px',
                'borderRadius': '6px',
                'border': f'2px solid {NAVY}',
                'cursor': 'pointer',
                'transition': 'all 0.3s ease',
            },
            n_clicks=0
        ),
        
        # Forgot Password Link
        html.Div([
            html.A("Forgot password?", href="#", style={
                'fontSize': '13px', 'color': PRIMARY, 'textDecoration': 'none', 
                'marginTop': '16px', 'display': 'block', 'fontWeight': '500',
                'transition': 'color 0.3s ease',
            }),
        ]),
    ])


def _get_signup_form():
    """Sign Up form component"""
    return html.Div([
        # Full Name
        html.Div([
            html.Label("Full Name", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signup-name',
                type='text',
                placeholder='Enter your full name',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Email
        html.Div([
            html.Label("Email Address", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signup-email',
                type='email',
                placeholder='Enter your email',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Username
        html.Div([
            html.Label("Username", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signup-username',
                type='text',
                placeholder='Choose a username',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Password
        html.Div([
            html.Label("Password", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signup-password',
                type='password',
                placeholder='Create a password (min. 8 chars)',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Confirm Password
        html.Div([
            html.Label("Confirm Password", style={
                'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 
                'display': 'block', 'marginBottom': '8px'
            }),
            dcc.Input(
                id='auth-signup-password-confirm',
                type='password',
                placeholder='Confirm password',
                style={
                    'padding': '12px 14px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '15px',
                    'boxSizing': 'border-box',
                    'width': '100%',
                    'fontFamily': 'inherit',
                }
            ),
        ], style={'marginBottom': '25px'}),
        
        # Create Account Button
        dbc.Button(
            "Create Account",
            id='auth-btn-signup',
            size='lg',
            style={
                'width': '100%',
                'backgroundColor': NAVY,
                'borderColor': NAVY,
                'color': '#FFFFFF',
                'fontWeight': '700',
                'fontSize': '15px',
                'padding': '12px 16px',
                'borderRadius': '6px',
                'border': f'2px solid {NAVY}',
                'cursor': 'pointer',
                'transition': 'all 0.3s ease',
            },
            n_clicks=0
        ),
    ])


# ════════════════════════════════════════════════════════════════
# CALLBACKS
# ════════════════════════════════════════════════════════════════

@callback(
    [Output('auth-signin-form-container', 'style'),
     Output('auth-signup-form-container', 'style'),
     Output('auth-btn-signin-tab', 'style'),
     Output('auth-btn-signup-tab', 'style')],
    [Input('auth-btn-signin-tab', 'n_clicks'),
     Input('auth-btn-signup-tab', 'n_clicks')],
    prevent_initial_call=False
)
def switch_auth_tabs(signin_clicks, signup_clicks):
    """Switch between Sign In and Sign Up forms"""
    signin_active = (signin_clicks or 0) >= (signup_clicks or 0)
    
    signin_style = {
        'background': 'none',
        'border': 'none',
        'fontSize': '18px',
        'fontWeight': '700',
        'color': NAVY if signin_active else TEXT_LIGHT,
        'cursor': 'pointer',
        'paddingBottom': '12px',
        'borderBottom': f'3px solid {NAVY}' if signin_active else 'none',
        'transition': 'all 0.3s ease',
    }
    
    signup_style = {
        'background': 'none',
        'border': 'none',
        'fontSize': '18px',
        'fontWeight': '700',
        'color': NAVY if not signin_active else TEXT_LIGHT,
        'cursor': 'pointer',
        'paddingBottom': '12px',
        'transition': 'all 0.3s ease',
    }
    
    return (
        {'display': 'block'} if signin_active else {'display': 'none'},
        {'display': 'block'} if not signin_active else {'display': 'none'},
        signin_style,
        signup_style,
    )
