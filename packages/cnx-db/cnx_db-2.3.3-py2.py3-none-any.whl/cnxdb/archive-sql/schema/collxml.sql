SELECT 
  xmlelement(name "col:collection",
             xmlattributes( 'http://cnx.rice.edu/collxml' as "xmlns",
                            'http://cnx.rice.edu/cnxml' as "xmlns:cnx",
                            'http://cnx.rice.edu/system-info' as "xmlns:cnxorg",
                            'http://cnx.rice.edu/mdml' as "xmlns:md",
                            'http://cnx.rice.edu/collxml' as "xmlns:col",
                            m.language as "xml:lang"),
  xmlelement(name "metadata", 
             xmlattributes('http://cnx.rice.edu/mdml' as "xmlns:md",
                           '0.5' as "mdml-version"),
      xmlcomment(E' WARNING! The \'metadata\' section is read only. Do not edit below. Changes to the metadata section in the source will not be saved. '),

      xmlelement(name "md:repository", 'https://legacy-dev.cnx.org/content'),
      xmlelement(name "md:content-url", 'https://legacy-dev.cnx.org/content/' || m.moduleid||'/'|| m.version),

      xmlelement(name "md:content-id", m.moduleid),
      xmlelement(name "md:title", m.name),
      
      xmlelement(name "md:version", m.version),
      xmlelement(name "md:created", m.created),
      xmlelement(name "md:revised", m.revised),
      xmlelement(name "md:language", m.language),

      xmlelement(name "md:license", xmlattributes( l.url as "url"),
        l.name),

      xmlcomment(E' For information on license requirements for use or modification, see license url in the above <md:license> element.
           For information on formatting required attribution, see the URL:
             CONTENT_URL/content_info#cnx_cite_header
           where CONTENT_URL is the value provided above in the <md:content-url> element.
      '),
      

      xmlelement(name "md:actors",
        (SELECT xmlagg(
            xmlelement(name "md:person", xmlattributes( a.personid as "userid"),
              xmlelement(name "md:firstname", a.firstname),
              xmlelement(name "md:surname", a.surname),
              xmlelement(name "md:fullname", a.fullname),
              xmlelement(name "md:email", a.email))
            ) FROM ( SELECT distinct p.* from persons p,
                moduleoptionalroles mor 
                right join modules mod on mor.module_ident = mod.module_ident
                WHERE 

                (p.personid = any (mod.authors) or 
                    p.personid = any (mod.maintainers) or
                    p.personid = any (mod.licensors) or
                    p.personid = any (mor.personids)
                )

                and mod.module_ident = m.module_ident
                  ) as a
          )
      ),

      xmlelement(name "md:roles",
            xmlelement(name "md:role", xmlattributes( 'authors' as "type"), array_to_string(m.authors,' ')),
            xmlelement(name "md:role", xmlattributes( 'maintainers' as "type"), array_to_string(m.maintainers,' ')),
            xmlelement(name "md:role", xmlattributes( 'licensors' as "type"), array_to_string(m.licensors,' ')),
            (SELECT xmlelement(name "md:role", xmlattributes( roleparam as "type"), array_to_string(personids, ' ')) FROM
                roles r join moduleoptionalroles mor on r.roleid = mor.roleid WHERE mor.module_ident = m.module_ident
            )
      ),
      xmlelement(name "md:abstract", ab.abstract),
      xmlelement(name "md:subjectlist",
        (SELECT xmlagg(
            xmlelement(name "md:subject", t.tag)
            )
            FROM moduletags mt join tags t on mt.tagid = t.tagid
            WHERE mt.module_ident = m.module_ident and t.scheme = 'ISKME subject'
        )
      ),
      xmlelement(name "md:keywordlist",
        (SELECT xmlagg(
            xmlelement(name "md:keyword", k.word)
            )
            FROM modulekeywords mk join keywords k on mk.keywordid = k.keywordid
            WHERE mk.module_ident = m.module_ident
        )
      )

  )
)
FROM
    modules m 
        join licenses l on m.licenseid = l.licenseid
        join abstracts ab on m.abstractid = ab.abstractid
WHERE 
    ident_hash(uuid, major_version, minor_version) = '383d4b87-2d7b-454e-99fe-2eaa43eae8ff@20.20'

GROUP BY m.module_ident, m.moduleid, m.name, m.version, m.created, m.revised, m.language, l.url, l.name, ab.abstract
