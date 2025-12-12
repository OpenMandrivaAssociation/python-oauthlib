%global pypi_name oauthlib

Name:           python-%{pypi_name}
Version:	3.2.2
Release:	4
Summary:        Implementation of the OAuth request signing logic
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/oauthlib
Source0:	https://files.pythonhosted.org/packages/source/o/oauthlib/oauthlib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)

%description
OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for handling OAuth requests, but they all suffer from
one or both of the following:

They predate the OAuth 1.0 spec, AKA RFC 5849.
They predate the OAuth 2.0 spec, AKA RFC 6749.
They assume the usage of a specific HTTP request library.

OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without
assuming a specific HTTP request object or web framework. Use it to graft OAuth
client support onto your favorite HTTP library, or provide support onto your
favourite web framework. If you're a maintainer of such a library, write a
thin veneer on top of OAuthLib and get OAuth support for very little effort.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
