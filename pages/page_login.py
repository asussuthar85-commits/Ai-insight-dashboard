"""
Login and Signup Page
Handles user authentication UI
"""

import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, callback
import dash
from core.config import NAVY, GOLD, PRIMARY_BG, CARD_BG, TEXT, TEXT_LIGHT, BORDER, PRIMARY


def generate_login_page():
    """Generate login page layout"""
    
    return dbc.Container([
        dcc.Location(id='url-login', refresh=False),
        
        dbc.Row([
            dbc.Col([
                # Left Side - Branding
                html.Div([
                    html.Div([
                        html.Div("◆", style={'fontSize': '48px', 'color': GOLD, 'marginBottom': '10px'}),
                        html.H1("ONEX AI", style={'color': '#FFFFFF', 'fontWeight': '700', 'marginBottom': '4px'}),
                        html.P("Data Insight", style={'color': GOLD, 'fontSize': '14px', 'fontWeight': '600', 'margin': '0'}),
                    ], style={'textAlign': 'center', 'marginBottom': '40px'}),
                    
                    html.Div([
                        html.H3("AI-Powered Dashboard", style={'color': '#FFFFFF', 'fontWeight': '700', 'marginBottom': '20px'}),
                        html.Ul([
                            html.Li("Auto-detect data patterns", style={'color': TEXT_LIGHT, 'marginBottom': '12px', 'fontSize': '14px'}),
                            html.Li("Generate insightful dashboards", style={'color': TEXT_LIGHT, 'marginBottom': '12px', 'fontSize': '14px'}),
                            html.Li("Connect multiple data sources", style={'color': TEXT_LIGHT, 'marginBottom': '12px', 'fontSize': '14px'}),
                            html.Li("AI-powered recommendations", style={'color': TEXT_LIGHT, 'marginBottom': '12px', 'fontSize': '14px'}),
                        ], style={'paddingLeft': '20px', 'listStyleType': 'none'}),
                    ]),
                ], style={
                    'backgroundColor': NAVY,
                    'padding': '60px 40px',
                    'minHeight': '100vh',
                    'display': 'flex',
                    'flexDirection': 'column',
                    'justifyContent': 'center',
                    'color': '#FFFFFF',
                }),
            ], xs=12, md=6, style={'padding': '0'}),
            
            # Right Side - Login Form
            dbc.Col([
                html.Div([
                    # Tab Selection
                    dbc.Row([
                        dbc.Col([
                            html.Button(
                                "Sign In",
                                id='btn-login-tab',
                                n_clicks=1,
                                style={
                                    'background': 'none',
                                    'border': 'none',
                                    'fontSize': '18px',
                                    'fontWeight': '700',
                                    'color': NAVY,
                                    'cursor': 'pointer',
                                    'paddingBottom': '10px',
                                    'borderBottom': f'3px solid {NAVY}',
                                }
                            ),
                        ], width=6),
                        dbc.Col([
                            html.Button(
                                "Sign Up",
                                id='btn-signup-tab',
                                n_clicks=0,
                                style={
                                    'background': 'none',
                                    'border': 'none',
                                    'fontSize': '18px',
                                    'fontWeight': '700',
                                    'color': TEXT_LIGHT,
                                    'cursor': 'pointer',
                                    'paddingBottom': '10px',
                                }
                            ),
                        ], width=6),
                    ], style={'borderBottom': f'2px solid {BORDER}', 'marginBottom': '40px'}),
                    
                    # Login Form - Pre-populated with initial form
                    html.Div(id='login-form-container', children=get_login_form(), style={'display': 'block'}),

                    # Signup Form - Initially empty
                    html.Div(id='signup-form-container', children=None, style={'display': 'none'}),
                    
                    # Error Alert
                    html.Div(id='auth-error-message', style={'marginTop': '20px'}),
                    
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


def get_login_form():
    """Return login form HTML"""
    return html.Div([
        # Username
        html.Div([
            html.Label("Username", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='login-username',
                type='text',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '20px'}),
        
        # Password
        html.Div([
            html.Label("Password", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='login-password',
                type='password',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '30px'}),
        
        # Sign In Button as Link
            dbc.Button(
                "Sign In",
                id='btn-sign-in',
                size='lg',
                style={
                    'width': '100%',
                    'backgroundColor': NAVY,
                    'borderColor': NAVY,
                    'color': '#FFFFFF',
                    'fontWeight': '700',
                    'fontSize': '14px',
                    'padding': '8px',
                },
                n_clicks=0
            ),
        
        # Forgot Password Link
        html.Div([
            html.A("Forgot password?", href="#", style={'fontSize': '14px', 'color': PRIMARY, 'textDecoration': 'none', 'marginTop': '15px', 'display': 'block'}),
        ]),
    ])


def get_signup_form():
    """Return signup form HTML"""
    return html.Div([
        # Name
        html.Div([
            html.Label("Name", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='signup-firstname',
                type='text',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Email
        html.Div([
            html.Label("Email Address", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='signup-email',
                type='email',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Username
        html.Div([
            html.Label("Username", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='signup-username',
                type='text',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Password
        html.Div([
            html.Label("Password", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='signup-password',
                type='password',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '15px'}),
        
        # Confirm Password
        html.Div([
            html.Label("Confirm Password", style={'fontSize': '14px', 'fontWeight': '600', 'color': TEXT, 'display': 'block', 'marginBottom': '6px'}),
            dcc.Input(
                id='signup-password-confirm',
                type='password',
                style={
                    'padding': '2px 8px',
                    'borderRadius': '6px',
                    'border': f'1px solid {BORDER}',
                    'fontSize': '16px',
                    'boxSizing': 'border-box',
                    'height': '50px',
                    'minHeight': '50px',
                }
            ),
        ], style={'marginBottom': '30px'}),
        
        # Sign Up Button as Link
            dbc.Button(
                "Create Account",
                id='btn-sign-up',
                size='lg',
                style={
                    'width': '100%',
                    'backgroundColor': NAVY,
                    'borderColor': NAVY,
                    'color': '#FFFFFF',
                    'fontWeight': '700',
                    'fontSize': '14px',
                    'padding': '8px',
                },
                n_clicks=0
            ),
    ])

# ════════════════════════════════════════════════════════════════
# CALLBACKS FOR TAB SWITCHING
# ════════════════════════════════════════════════════════════════

@callback(
    [Output('login-form-container', 'children'),
    Output('login-form-container', 'style'),
    Output('signup-form-container', 'children'),
    Output('signup-form-container', 'style'),
    Output('btn-login-tab', 'style'),
    Output('btn-signup-tab', 'style')],
    [Input('btn-login-tab', 'n_clicks'),
    Input('btn-signup-tab', 'n_clicks')],
    prevent_initial_call=False
)
def switch_auth_tabs(login_clicks, signup_clicks):
    """Switch between login and signup forms"""
    
    # Determine which tab should be active
    login_active = (login_clicks or 0) >= (signup_clicks or 0)
    
    login_style = {
        'background': 'none',
        'border': 'none',
        'fontSize': '18px',
        'fontWeight': '700',
        'color': NAVY if login_active else TEXT_LIGHT,
        'cursor': 'pointer',
        'paddingBottom': '10px',
        'borderBottom': f'3px solid {NAVY}' if login_active else 'none',
        'transition': 'all 0.3s ease',
    }
    
    signup_style = {
        'background': 'none',
        'border': 'none',
        'fontSize': '18px',
        'fontWeight': '700',
        'color': NAVY if not login_active else TEXT_LIGHT,
        'cursor': 'pointer',
        'paddingBottom': '10px',
        'transition': 'all 0.3s ease',
    }
    
    login_container_style = {'display': 'block'} if login_active else {'display': 'none'}
    signup_container_style = {'display': 'block'} if not login_active else {'display': 'none'}
    
    return (
        get_login_form(),         # ✅ CALL the function
        login_container_style,
        get_signup_form(),        # ✅ CALL the function
        signup_container_style,
        login_style,
        signup_style
    )


# ════════════════════════════════════════════════════════════════
# LOGIN CALLBACK
# ════════════════════════════════════════════════════════════════

# @callback(
#     Output('url', 'pathname'),  # ✅ Navigate to a new page
#     Input('btn-sign-in', 'n_clicks'),
#     [State('login-username', 'value'),
#     State('login-password', 'value')],
#     prevent_initial_call=True
# )
# def handle_sign_in(n_clicks, username, password):
#     """Handle Sign In - validate and navigate to upload page"""
#     if not n_clicks:
#         raise dash.exceptions.PreventUpdate
    
#     # Simple validation
#     if not username or not password:
#         raise dash.exceptions.PreventUpdate
    
#     # TODO: Add actual authentication logic here
#     print(f"[AUTH] User '{username}' signed in")
#     return '/upload'  # ✅ Navigate to upload page

# # ════════════════════════════════════════════════════════════════
# # SIGN UP CALLBACK - Navigate to Upload Page
# # ════════════════════════════════════════════════════════════════

# @callback(
#     Output('url', 'pathname', allow_duplicate=True),  # ✅ Use allow_duplicate for multiple callbacks
#     Input('btn-sign-up', 'n_clicks'),
#     [State('signup-firstname', 'value'),
#     State('signup-email', 'value'),
#     State('signup-username', 'value'),
#     State('signup-password', 'value'),
#     State('signup-password-confirm', 'value')],
#     prevent_initial_call=True
# )
# def handle_sign_up(n_clicks, fullname, email, username, password, password_confirm):
#     """Handle Sign Up - validate and navigate to upload page"""
#     if not n_clicks:
#         raise dash.exceptions.PreventUpdate
    
#     # Simple validation
#     if not fullname or not email or not username or not password or not password_confirm:
#         raise dash.exceptions.PreventUpdate
    
#     # Validate passwords match
#     if password != password_confirm:
#         print("[AUTH] Passwords do not match")
#         raise dash.exceptions.PreventUpdate
    
#     # Validate password length
#     if len(password) < 8:
#         print("[AUTH] Password must be at least 8 characters")
#         raise dash.exceptions.PreventUpdate
    
#     # TODO: Add actual user registration logic here
#     print(f"[AUTH] New user '{username}' ({email}) registered")
#     return '/upload'  # ✅ Navigate to upload page